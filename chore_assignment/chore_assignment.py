#! /usr/bin/env python3
# chore_assignment.py - randomly assigns predefined chores and notifies via email

import random
import smtplib
from os import environ


def allocate_chores(chores, emails):
    """
    Allocates chores randomly to the various emails

    :param list chores: list of chores
    :param list emails: list of participants' emails
    """
    chore_assignments = dict()

    for email in email_generator(emails=emails):
        if not chores:
            break

        chore_assignment = random.choice(chores)
        chores.remove(chore_assignment)

        chore_assignments.setdefault(email, [])
        chore_assignments[email].append(chore_assignment)

    return chore_assignments


def email_generator(emails):
    """
    Shuffles the emails, then after iterating through the entire list,
    shuffles the emails again.

    This results in a somewhat random allocation while keeping the quantity
    of chores assigned to each individual consistent.

    :param list emails: list of participants' emails
    """
    while True:
        random.shuffle(emails)
        yield from emails


def email_assigned_chores(chore_assignments):
    """
    Emails each participant with the list of assigned chores

    :param dict chore_assignments: structure that holds all of the allocated chores
                in the form {email: [chores]}
    """
    email = environ.get('AUTO_EMAIL')
    password = environ.get('EMAIL_CREDENTIALS')

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, password)

    for recipient, chores in chore_assignments.items():
        message = f'To: {recipient}' \
            f'\nSubject: Chore Assignments' \
            f'\nGreetings,' \
            f'\n\nYour assigned chores are: {format_chores(chores=chores)}.'

        sendmail_status = smtp.sendmail(email, recipient, message)

        if sendmail_status != {}:
            print(f'There was a problem sending an email to {recipient} - {sendmail_status}')

    smtp.quit()


def format_chores(chores):
    """
    Formats the chores to properly utilize the Oxford comma

    :param list chores: list of chores
    """
    if len(chores) == 1:
        return f'{chores[0]}'
    elif len(chores) == 2:
        return f'{chores[0]} and {chores[1]}'
    else:
        chores[-1] = 'and ' + chores[-1]
        return f"{', '.join(chores)}"


if __name__ == '__main__':
    chore_list = ['wash dishes', 'clean bathroom', 'vacuum', 'walk the dog',
                  'take out the trash', 'take out the recycling', 'get the mail',
                  'clean the fish tank', 'cook dinner', 'set the table']
    email_list = ['resident01@example.com', 'resident02@example.com',
                  'resident03@example.com', 'resident04@example.com']

    assignments = allocate_chores(chores=chore_list, emails=email_list)
    email_assigned_chores(chore_assignments=assignments)
