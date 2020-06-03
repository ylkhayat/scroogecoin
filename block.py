class Block():
    """ 
    Class represents a single block containing an amount of transactions to be soon added into the ledger.
    Each block will contain 10 transactions and will have a pointer to the hash of the previous block.
    """
    # constructor method handling the initiation process of the block.
    def __init__(self, transactions = [], hash_prev_block = None):
        self.transactions = transactions
        self.hash_prev_block = hash_prev_block

    # method responsible for adding an already created transaction to the block, returns a boolean in case of the limit was exceeded.
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        return len(self.transactions) != 10

    # toString method handling the string representation of the block.
    def __str__(self):
        separator = '-' * 50 +'\n'
        hash_prev_block_str = 'Previous Block Hash: ' + (str(self.hash_prev_block) or 'None') +'\n'
        string = 'Block Content: \n' + hash_prev_block_str
        for ind,transaction in enumerate(self.transactions):
            string += str(ind) +'. ' + str(transaction) + separator
        return string

    def get_balance(self, pubk):
        in_coins = []
        out_coins = []
        for transaction in self.transactions:
            coins = transaction.coins
            if transaction.receiver == pubk:
                in_coins += coins
            if transaction.sender == pubk:
                in_coins += coins
        return in_coins, out_coins

    def is_double_spending(self, transaction):
        for transaction_coin in transaction.coins:
            for stored_transaction in self.transactions:
                for stored_coin in stored_transaction.coins:
                        if(transaction_coin.id == stored_coin.id and transaction_coin.user_id == stored_coin.user_id):
                            return True
        return False

