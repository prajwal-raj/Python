#! /usr/bin/env python3
# form_filler.py -

from pathlib import Path
from time import sleep

import pyautogui


def fill_forms(field_position, data, paths):
    submit_another = None

    for person in data:
        print('>>> 3 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
        sleep(3)
        fill_form(field_position=field_position, data=person)
        print('Submitted form.')
        sleep(3)
        if not submit_another:
            submit_another = submit_another_coords(*paths)
        pyautogui.click(submit_another)


def fill_form(field_position, data):
    print(f'Entering {data["name"]} info...')
    pyautogui.doubleClick(field_position)

    pyautogui.typewrite(f'{data["name"]}\t')
    pyautogui.typewrite(f'{data["fear"]}\t')
    pyautogui.typewrite(drop_down_menu(text=data['source']), interval=0.5)
    pyautogui.typewrite(radio_button(value=data['robocop']), interval=0.25)
    pyautogui.typewrite(f'{data["comments"]}\t')
    pyautogui.press('enter')


def drop_down_menu(text):
    if text == 'wand':
        return ['down', 'enter', 'tab']
    elif text == 'amulet':
        return ['down', 'down', 'enter', 'tab']
    elif text == 'crystal ball':
        return ['down', 'down', 'down', 'enter', 'tab']
    elif text == 'money':
        return ['down', 'down', 'down', 'down', 'enter', 'tab']


def radio_button(value):
    if value == 1:
        return [' ', 'tab']
    elif value == 2:
        return ['right', 'tab']
    elif value == 3:
        return ['right', 'right', 'tab']
    elif value == 4:
        return ['right', 'right', 'right', 'tab']
    elif value == 5:
        return ['right', 'right', 'right', 'right', 'tab']


def submit_another_coords(path1, path2):
    submit_link = pyautogui.center(pyautogui.locateOnScreen(str(path1)))  # lgtm [py/call/wrong-arguments]
    if submit_link:
        return submit_link
    else:
        return pyautogui.center(pyautogui.locateOnScreen(str(path2)))  # lgtm [py/call/wrong-arguments]


if __name__ == '__main__':
    name_field = pyautogui.center(
        pyautogui.locateOnScreen(str(Path('images/name_field.png'))))  # lgtm [py/call/wrong-arguments]
    pyautogui.PAUSE = 0.5

    form_data = [{'name':     'Alice',
                  'fear':     'eavesdroppers',
                  'source':   'wand',
                  'robocop':  4,
                  'comments': 'Tell Bob I said hi.'},
                 {'name':     'Bob',
                  'fear':     'bees',
                  'source':   'amulet',
                  'robocop':  4,
                  'comments': 'n/a'},
                 {'name':     'Carol',
                  'fear':     'puppets',
                  'source':   'crystal ball',
                  'robocop':  1,
                  'comments': 'Please take the puppets out of the break room.'},
                 {'name':     'Alex Murphy',
                  'fear':     'ED-209',
                  'source':   'money',
                  'robocop':  5,
                  'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}]

    images = [Path('images/submit_another1.png').resolve(),
              Path('images/submit_another2.png').resolve()]

    fill_forms(field_position=name_field, data=form_data, paths=images)
