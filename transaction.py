class Transaction():
    """ 
    Class represents a single transaction, signed by the user creating it.
    """
    def __init__(self, coins, receiver, previous_transaction_hash=None, genre="transfer"):
        self.id = self.__str__().__hash__()
        self.coins = coins
        self.previous_transaction_hash = previous_transaction_hash
        self.receiver = receiver
        self.genre = genre
        self.hash_val = None

    def hash(self, hash):
        self.hash_val = hash

    def __str__(self):
        return 'Transaction ID:\t' + str(self.id) + '\nHash(Previous Transaction): ' + self.previous_transaction_hash + '\nAmount: '+ str(len(self.coins)) + '\tGenre: '+ self.genre + '\nCoins: ' + "".join(map(str, self.coins)) + '\n\n'

        