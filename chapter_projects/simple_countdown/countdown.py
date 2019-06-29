#! /usr/bin/env python3
# countdown.py - a simple countdown script

import time
import subprocess


def countdown(seconds=60):
    for x in range(seconds, 0, -1):
        print(f'{reset_line}{x} seconds', end='', flush=True)
        time.sleep(1)

    print(f'{reset_line}Alarm!')
    subprocess.Popen(['open', 'alarm.wav'])


if __name__ == '__main__':
    reset_line = '\u001b[2K\u001b[20D'
    countdown(15)
