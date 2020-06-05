from scrooge import Scrooge
from user import User
from tools import OUTPUT_PATH, logger

import keyboard
import random
import time

from os import _exit

NUMBER_OF_WALLETS = 10


if __name__ == '__main__':

    open(OUTPUT_PATH, 'w').close()

    users = [User() for _ in range(NUMBER_OF_WALLETS)]
    scrooge = Scrooge(users)

    def on_space_press(_):
        logger("Wrap up! Check your `./output/log.txt` file for logs.")
        scrooge.sign_last_block()
        # logger('\nLast block successfully signed:\t'+scrooge.current_building_block.signature)
        _exit(0)


    keyboard.on_press_key("space", on_space_press)

    while(True):
        sender = random.randint(0, NUMBER_OF_WALLETS - 1)
        receiver = random.randint(0, NUMBER_OF_WALLETS - 1)
        
        users[sender].create_transaction(
            users[receiver], scrooge)
    
        time.sleep(0.2)