from transaction import Transaction
from tools import gen_keys, sign, get_hash, logger
import random

class User():
    def __init__(self):
        self.__private_key, self.public_key = gen_keys()
        self.id = self.public_key
        self.coins = []

    def create_transaction(self, receiver, scrooge):
        list_coins = self.balance(scrooge)
        if(receiver.public_key == self.public_key):
            logger('*'*20 + '\nTransaction Aborted\nSelf Transfer is not Allowed\nFrom:\t' + str(self.id.__hash__()) + '\nTo:\t' + str(receiver.id.__hash__())+'\n'+'*'*20)
            return
        if len(list_coins) == 0:
            logger('|TRANSACTION REJECTED\t-\tInsuficient Balance|')
            return

        transfer_coin_index = random.randint(0, len(list_coins) - 1)
        transfer_coin = list_coins[transfer_coin_index]
        transaction = Transaction(self.public_key, [transfer_coin], receiver.public_key)
        if self.__sign( transaction):
            logger('*'*20 + '\nTransaction Created\nFrom:\t' + str(self.id.__hash__()) + '\nTo:\t' + str(receiver.id.__hash__())+'\n'+'*'*20)
            scrooge.process_transaction(transaction, self.public_key)

    def add_transaction(self, coins):
        for coin in coins:
            self.coins.append(coin)
            coin.change_ownership(self.id)
        logger('User:\t\t' + str(self.id.__hash__()) + '\nReceived:\t' + str(len(coins))+' coin(s)\n')

    def balance(self, scrooge):
        return scrooge.blockchain.get_balance(self.public_key)

    def __sign(self, transaction):
        try:
            transaction_content = get_hash(transaction)
            signature = sign(self.__private_key, transaction_content)
            transaction.add_signing(signature)
            transaction.add_hash(transaction_content)
            return True
        except:
            return False