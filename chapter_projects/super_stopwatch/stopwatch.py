#! /usr/bin/env python3
# stopwatch.py - a simple stopwatch program

import time


def print_instructions():
    input("Press ENTER to begin."
          "\nAfterwards, press enter to 'click' the stopwatch."
          "\nPress Ctrl + C to quit.\n")
    print('Starting.\n')


def table_seperator(begin='╠', middle='╬', end='╣'):
    return f"{begin}{'═' * 14}{middle}{'═' * 20}{middle}{'═' * 18}{end}"


def stopwatch():
    start = time.time()
    previous_time = start
    lap_num = 1
    spacer = '  ║  '

    # print table header
    print(f"{table_seperator(begin='╔', middle='═', end='╗')}"
          f"\n║{'Super Stopwatch':^54}║"
          f"\n{table_seperator(middle='╦')}"
          f"\n║{'Lap Number':^14}║ "
          f"{'Total time':^19}║ "
          f"{'Lap Time':^17}║"
          f"\n{table_seperator()}", end='')

    try:
        while True:
            input()
            lap_time = f'{time.time() - previous_time:,.2f} s'
            total_time = f'{time.time() - start:,.2f} s'
            print(f"║  Lap #{lap_num:<5}{spacer}"
                  f"{total_time:>16}{spacer}"
                  f"{lap_time:>14}  ║", end='')
            lap_num += 1
            previous_time = time.time()
    except KeyboardInterrupt:
        print(f"\n╚{'═' * 14}╩{'═' * 20}╩{'═' * 18}╝"
              f"\n\nDone.")


if __name__ == '__main__':
    print_instructions()
    stopwatch()