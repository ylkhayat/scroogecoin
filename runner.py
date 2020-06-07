from scrooge import Scrooge
from user import User
from tools import OUTPUT_PATH, logger

import keyboard
import random
import time

from os import _exit

NUMBER_OF_USERS = 10


if __name__ == '__main__':

    open(OUTPUT_PATH, 'w').close()

    users = [User() for _ in range(NUMBER_OF_USERS)]
    scrooge = Scrooge(users)

    def on_space_press(_):
        logger("Wrap up! Check your `./output/log.txt` file for logs.")
        scrooge.sign_last_block()
        # logger('\nLast block successfully signed:\t'+scrooge.current_building_block.signature)
        _exit(0)

    keyboard.on_press_key("space", on_space_press)
    while(True):
        sender_index = random.randint(0, NUMBER_OF_USERS - 1)
        receiver_index = random.randint(0, NUMBER_OF_USERS - 1)
        users[sender_index].create_transaction(
            users[receiver_index], scrooge)
        time.sleep(0.2)