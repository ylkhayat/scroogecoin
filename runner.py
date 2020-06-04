from scrooge import Scrooge
from user import User
from tools import OUTPUT_PATH

import keyboard
import random
import time

from os import _exit

NUMBER_OF_WALLETS = 10


if __name__ == '__main__':

    open(OUTPUT_PATH, 'w').close()

    wallets = [User() for _ in range(NUMBER_OF_WALLETS)]
    scrooge = Scrooge(wallets)

    def on_space_press(_):
        print("Wrap up!")
        _exit(0)

    keyboard.on_press_key("space", on_space_press)

    while(True):
        sender = random.randint(0, NUMBER_OF_WALLETS - 1)
        receiver = random.randint(0, NUMBER_OF_WALLETS - 1)
        
        wallets[sender].create_transaction(
            wallets[receiver], scrooge)
        time.sleep(2)