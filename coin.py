import uuid

class Coin():
    """
    Class representing the coin where each generated one has a unique identifier (using the uuid) and refers to the waller id it belongs to.
    """
    def __init__(self, wallet_id):
        self.wallet_id = wallet_id
        self.id = uuid.uuid1()

    def __str__(self):
        return 'Wallet ID: '+ self.wallet_id.__hash__() +' - id: ' + self.id

