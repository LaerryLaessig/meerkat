import logging

from flask_meerkat import mail, SERVER_DOMAIN


def send_new_task_mail(email):
    try:
        mail.send_message(
                recipients=[email],
                subject='New Task',
                body='Hi,\nyou have got a new task.\n Visit {url} to complete your task.'.format(url=SERVER_DOMAIN)
            )
    except AssertionError as e:
        logging.error('Failed to send mail: {}'.format(e))
