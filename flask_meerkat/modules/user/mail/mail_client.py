from flask_meerkat import mail


def send_password_reset_mail(email, link):
    mail.send_message(
                recipients=[email],
                subject='Passwort reset',
                body='Hi,\nhere your link to reset your password.\n {link}'.format(link=link)
            )
