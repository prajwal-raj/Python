#! /usr/bin/env python3
# looking_busy.py -

import random
from time import sleep

import pyautogui


def look_busy(interval=60):
    """
    Nudges the mouse by random x and y values (-10 to 10), then returns
    the mouse to it's original position. The duration of these moves is
    a random time value between 0.1 and 0.5 seconds.

    A function key bound to no action is chosen at random to simulate keyboard input

    :param float interval: max interval between mouse nudges
    """
    print('Press CTRL-C to quit.\n')
    try:
        while True:
            x = random.randint(a=-10, b=10)
            y = random.randint(a=-10, b=10)

            pyautogui.moveRel(xOffset=x, yOffset=y, duration=random.uniform(a=0.1, b=0.5))
            pyautogui.moveRel(xOffset=-x, yOffset=-y, duration=random.uniform(a=0.1, b=0.5))
            pyautogui.press(f'f{random.randint(15, 24)}')

            sleep(random.randint(a=interval // 2, b=interval))

    except KeyboardInterrupt:
        print('Process quit.')


if __name__ == '__main__':
    look_busy(interval=5 * 60)
