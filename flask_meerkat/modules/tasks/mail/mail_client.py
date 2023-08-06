import logging

from flask_meerkat import mail, SERVER_DOMAIN


def send_new_task_mail(email):
    try:
        mail.send_message(
                recipients=[email],
                subject='New Task',
                body=f'Hi,\nyou have got a new task.\n Visit {SERVER_DOMAIN} to complete your task.'
            )
    except AssertionError as e:
        logging.error(f'Failed to send mail: {e}')
