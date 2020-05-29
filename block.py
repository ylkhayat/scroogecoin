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
        if(len(self.transactions) < 10):
            self.transactions.append(transaction)
            return True
        else:
            return False

    # toString method handling the string representation of the block.
    def __str__(self):
        separator = '-' * 15 +'\n'
        hash_prev_block_str = 'Previous Block Hash: ' + (str(self.hash_prev_block) or 'None') +'\n'
        string = 'Block Content: \n' + hash_prev_block_str
        for transaction in self.transactions:
            string += str(transaction) + separator
        return string