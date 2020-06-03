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
        logger('\n' + '='*55 + '\nBlockChain Augmented\n' + '='*55 +'\n'+ str(self) +'='*80+'\n')

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
        for block in self.blocks:
            string += str(block) + separator
        return string