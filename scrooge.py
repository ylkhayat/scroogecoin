from blockchain import BlockChain
from block import Block
from transaction import Transaction
from coin import Coin

from tools import gen_keys, sign, verify, get_hash, logger

class Scrooge():
    """
    Class representing the maintainer Scrooge who will be monitoring every progress in his network and responsible for creating `Coin`s and verify transactions.
    This class possesses a private and a public key for its own authentications and 
    """
    def __init__(self, users):
        self.__private_key, self.public_key = gen_keys()
        self.blockchain = BlockChain()
        self.users = users
        self.current_building_block = Block()
        self.last_transaction = None
        self.last_block = None
        self.init()

    def process_transaction(self, transaction, sender_pubk):
        verified_check = self.verify_transaction(transaction, sender_pubk)
        double_spending_check = self.is_double_spending(transaction)
        if not verified_check:
            logger('|TRANSACTION REJECTED\t-\tInvalid Transaction|')
            return
        if double_spending_check:
            logger('|TRANSACTION REJECTED\t-\tDouble Spending Detected|\n|From User \t\t\t\t'+str(sender_pubk.__hash__())+'|')
            return
        transaction.add_prev_transaction(self.last_transaction)
        self.last_transaction = transaction.hash_val
        self.add_transaction_to_block(transaction)


    def create_coins(self, amount, user_id):
        return [Coin(user_id) for _ in range(amount)]

    def init(self):
        self.log_users()
        self.last_transaction = None
        for user in self.users:
            user_id = user.id
            coins = self.create_coins(10, 'scrooge')
            transaction = Transaction(
                self.public_key, coins, user_id, genre="create", previous_transaction_hash=self.last_transaction)
            if self.__sign(transaction):
                self.process_transaction(transaction, self.public_key)
    
    def log_users(self):
        logger('='*64+'\nUsers Report:\n'+'='*64)
        string_users = ''
        for user in self.users:
            string_users += user.to_string(self)
        logger(string_users+'\n'+'='*64)
    
    def add_coin_to_user(self, transaction):
        receiver_pubk = transaction.receiver
        transaction_coins = transaction.coins
        for user in self.users:
            if user.id == receiver_pubk:
                user.add_transaction(transaction_coins)
                break

    def add_transaction_to_block(self, transaction):
        if not self.current_building_block.add_transaction(transaction):
            self.last_block = self.current_building_block
            self.publish_block(self.current_building_block)
        
    def publish_block(self, block):
        self.blockchain.add_block(block)
        self.current_building_block = Block(transactions=[], hash_prev_block=self.last_block.id)
        for transaction in block.transactions:
            self.add_coin_to_user(transaction)
        self.log_users()



    def verify_transaction(self, transaction, sender_pk):
        return verify(sender_pk, transaction.signature, transaction.hash_val)

    def is_double_spending(self, transaction):
        return self.current_building_block.is_double_spending(transaction)
    
    def sign_last_block(self):
        self.__sign(self.current_building_block)

    def __sign(self, obj):
        if(isinstance(obj, Transaction)):
            try:
                transaction_content = get_hash(obj)
                signature = sign(self.__private_key, transaction_content)
                obj.add_signing(signature)
                obj.add_hash(transaction_content)
                return True
            except:
                return False
        else:
            try:
                block_content = get_hash(obj)
                signature = sign(self.__private_key, block_content)
                obj.add_signing(signature)
                return True
            except:
                return False

