import uuid

class Coin():
    """
    Class representing the coin where each generated one has a unique identifier (using the uuid) and refers to the waller id it belongs to.
    """
    static_variable = -1
    def __init__(self, user_id):
        # uid = uuid.uuid1()
        self.user_id = user_id
        # self.id = uid
        Coin.static_variable += 1
        self.id = Coin.static_variable

    def change_ownership(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return 'Coin \t' + str(self.id) + '\nProperty of\t'+ str(self.user_id.__hash__())+'\n'

