from scrooge import Scrooge
from user import User

import keyboard
import random
import time
from os import _exit

NUMBER_OF_WALLETS = 10
MIN_TRANSFET_AMOUNT = 1
MAX_TRANSFER_AMOUNT = 10

OUTPUT_PATH = "./output/log.txt"


if __name__ == '__main__':

    open(OUTPUT_PATH, 'w').close()

    wallets = [User() for _ in range(NUMBER_OF_WALLETS)]
    scrooge = Scrooge(wallets)

    def on_space_press(_):
        print("Wrap up!")
        _exit(0)

    keyboard.on_press_key("space", on_space_press)

    while(True):
        user_a = random.randint(0, NUMBER_OF_WALLETS - 1)
        user_b = random.randint(0, NUMBER_OF_WALLETS - 1)
        transfer_amount = random.randint(
            MIN_TRANSFET_AMOUNT, MAX_TRANSFER_AMOUNT)

        wallets[user_a].create_transaction(
            transfer_amount, wallets[user_b], scrooge)
        time.sleep(2)