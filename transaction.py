import uuid

class Transaction():
    """ 
    Class represents a single transaction, signed by the user creating it.
    """
    def __init__(self, sender, coins, receiver, previous_transaction_hash=None, genre="transfer"):
        self.coins = coins
        self.amount = len(coins)
        self.previous_transaction_hash = previous_transaction_hash
        self.sender = sender
        self.receiver = receiver
        self.genre = genre
        self.hash_val = None
        self.uid = uuid.uuid1().hex
        self.id = self.__str__().__hash__()
        
    def add_signing(self, signature_val):
         self.signature = signature_val

    def add_hash(self, hash_val):
        self.hash_val = hash_val

    def add_prev_transaction(self, prev_transaction):
        self.previous_transaction_hash = prev_transaction

    def has_coin(self, coin):
        for transaction_coin in self.coins:
            if transaction_coin.id == coin.id:
                return True
        return False

    def str_coins(self):
        return "".join(map(str, self.coins)) if isinstance(self.coins, list) else str(self.coins)

    def __str__(self):
        return 'Transaction UID: ' + str(self.uid) + '\nHash Transaction (Previous): ' + str(self.previous_transaction_hash) + '\nHash Transaction:\t'+str(self.hash_val) + '\nAmount: '+ str(self.amount) + ' coin(s)\tGenre: '+ self.genre

        