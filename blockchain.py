from block import Block

class BlockChain():
    """
    Class representing the ledger which is an array of blocks appended together.
    The ledger always saves the last appended block.
    """
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        self.blocks.append(block)

    def __str__(self):
        separator = '\n\n'
        string = 'BlockChain Content: \n' + separator
        for block in self.blocks:
            string += str(block) + separator
        return string