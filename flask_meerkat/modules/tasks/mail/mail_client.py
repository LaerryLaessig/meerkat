import logging

from flask_meerkat import mail, SERVER_DOMAIN


def send_new_task_mail(email, data):
    try:
        mail.send_message(
            recipients=[email],
            subject='New Task',
            body=create_body(data=data)
        )
    except AssertionError as e:
        logging.error(f'Failed to send mail: {e}')


def create_body(data):
    body = f'Hi,\nyou have got a new task.\n Visit {SERVER_DOMAIN} to complete your task.\n\n'
    body += f'{data["title"]}:\n\n'
    for s in data['subtasks']:
        body += f'- {s["subtask"]}\n'
    body += f'\nVisit {SERVER_DOMAIN} to complete your task.'
    return body
