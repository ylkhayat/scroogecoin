class Transaction():
    """ 
    Class represents a single transaction, signed by the user creating it.
    """
    def __init__(self, sender, coins, receiver, previous_transaction_hash=None, genre="transfer"):
        self.coins = coins
        self.previous_transaction_hash = previous_transaction_hash
        self.sender = sender
        self.receiver = receiver
        self.genre = genre
        self.hash_val = None
        self.id = self.__str__().__hash__()
        
    def add_signing(self, signature_val):
         self.signature = signature_val

    def add_hash(self, hash_val):
        self.hash_val = hash_val

    def add_prev_transaction(self, prev_transaction):
        self.previous_transaction_hash = prev_transaction

    def str_amount(self):
        return str(len(self.coins) if isinstance(self.coins, list) else 1)

    def str_coins(self):
        return "".join(map(str, self.coins)) if isinstance(self.coins, list) else str(self.coins)
    def __str__(self):
        return 'Transaction ID:\t'+str(self.hash_val)+'\nHash(Previous Transaction): ' + str(self.previous_transaction_hash) + '\nAmount: '+ self.str_amount() + '\tGenre: '+ self.genre + '\nCoins:\n' + self.str_coins()

        