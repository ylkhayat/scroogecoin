from block import Block
from tools import logger

class BlockChain():
    """
    Class representing the ledger which is an array of blocks appended together.
    The ledger always saves the last appended block.
    """
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        self.blocks.append(block)
        logger('\n' + '='*64 + '\n\t\t\t\tNEW BLOCK PUBLISHED\t\t\t\n' + '='*64 +'\n'+ str(self) +'='*64+'\n')

    def get_balance(self, pubk):
        saved_coins = []
        spent_coins = []
        for block in self.blocks:
            in_coins, out_coins = block.get_balance(pubk)
            saved_coins += in_coins
            spent_coins += out_coins
        for out_coin in spent_coins:
            saved_coins.remove(out_coin)
        return saved_coins

    def __str__(self):
        separator = '\n'
        string = 'BlockChain Content: \n' + separator
        for ind, block in enumerate(self.blocks):
            string += '\n' + '=' * 28 + 'Block ' + str(ind) +'=' * 28+'\n'+ str(block)
        return string