from flask_meerkat import mail


def send_password_reset_mail(email):
    mail.send_message(
                recipients=[email],
                subject='Passwort reset',
                body='''
                Hi, 
                
                here your link to reset your password.
                
                
                '''
            )
