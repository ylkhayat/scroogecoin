from transaction import Transaction
from signings import gen_keys, sign, get_hash

class User():
    def __init__(self):
        self.__private_key, self.public_key = gen_keys()
        self.id = self.public_key
        self.coins = []

    def create_transaction(self, receiver, scrooge):
        list_coins = self.coins
        if len(list_coins) > 0:
            return

        transfer_coin = list_coins[-1]
        transaction = Transaction(transfer_coin, receiver.public_key)
        if self.__sign( transaction):
            list_coins.pop()
            scrooge.process_transaction(transaction, self.public_key, receiver.public_key)

    def add_coin(self, coin):
        self.coins.append(coin)

    def __sign(self, transaction):
        try:
            transaction_content = get_hash(transaction)
            signature = sign(self.__private_key, transaction_content)
            transaction.__add_signing(signature)
            transaction.__add_hash(transaction_content)
            return True
        except:
            return False