from flask_meerkat import mail


def send_new_task_mail(email):
    mail.send_message(
                recipients=[email],
                subject='New Task',
                body='Hi,\nyou have got a new task.\n'.format()
            )
