from blockchain import BlockChain
from block import Block
from transaction import Transaction
from coin import Coin

from signings import gen_keys, sign, verify, get_hash

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
        self.init()

    def process_transaction(self, transaction, sender_pubk):
        verified_check = self.verify_transaction(transaction, sender_pubk)
        double_spending_check = self.is_double_spending(transaction)
        if not verified_check and double_spending_check:
            return
        self.add_transaction_to_block(transaction)


    def create_coins(self, amount, user_id):
        return [Coin(user_id) for _ in range(amount)]

    def init(self):
        previous_transaction_hash = None
        for user in self.users:
            user_id = user.id
            coins = self.create_coins(10, user_id)
            transaction = Transaction(
                coins, user.id, genre="create", previous_transaction_hash=previous_transaction_hash)
            transaction.previous_transaction_hash = previous_transaction_hash
            if self.__sign(transaction):
                previous_transaction_hash = transaction.hash_val
                self.add_transaction_to_block(transaction)
    
    def add_transaction_to_block(self, transaction):
        if not self.current_building_block.add_transaction(transaction):
                    self.blockchain.add_block(self.current_building_block)
                    self.current_building_block = Block()
                    self.last_transaction = transaction

    def verify_transaction(self, transaction, sender_pk):
        return verify(sender_pk, transaction.signature, transaction.hash_val)

    def is_double_spending(self, transaction):
        return self.current_building_block.is_double_spending(transaction)
        
    def __sign(self, transaction):
        try:
            transaction_content = get_hash(transaction)
            signature = sign(self.__private_key, transaction_content)
            transaction.__add_signing(signature)
            transaction.__add_hash(transaction_content)
            return True
        except:
            return False

