# Simple blog and task manage system

Website to create blog posts and tasks for different user.

## enviroment variables
- SECRET_KEY
  - change in start.sh or in enviroment variable
  - default value secret_key
- MAIL_USERNAME
  - change in start.sh or in enviroment variable
  - mail account for password reset and inform about new task
  - default value ''
- MAIL_PASSWORD
  - change in start.sh or in enviroment variable
  - default value ''
- MAIL_DEFAULT_SENDER
  - change in start.sh or in enviroment variable
  - mail adress for password reset and inform about new task
  - default value ''

## functions
- sign up
  - only whitelisted user can sign up
  - the first sign up user is automatically on the whitelist
  - first sign up user is the admin
- whitelist
  - the admin can manage the whitelist
- post
  - all registered user can manage posts
- task
  - all registered user can create tasks
  - user can see and edit task if they are the reviser or creator of the task
- account
  - user can edit there username and email address

## dependencies
- flask
  - micro web framework
  - https://palletsprojects.com/p/flask/
- flask-bcrypt
  - extension to provides bcrypt hashing utilities 
  - https://flask-bcrypt.readthedocs.io/en/latest/
- flask_httpauth
  - extension that simplifies the use of HTTP authentication with Flask routes
  - https://flask-httpauth.readthedocs.io/en/latest/
- flask sqlalchemy
  - extension that simplifies using SQLAlchemy
  - https://flask-sqlalchemy.palletsprojects.com/
- flask_bootstrap
  - extension that simplifies using bootstrap4
  - https://github.com/mbr/flask-bootstrap
- flask-login
  - extension that simplifies manage user sessions 
  - https://flask-login.readthedocs.io/en/latest/
- flask-mailer 
  - extension that simplifies to send emails to user 
  - https://pythonhosted.org/Flask-Mail/
- flask-wtf
  - simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA
  - https://flask-wtf.readthedocs.io/en/latest/
- flask-fontawesome
  - extension that simplifies using fontawesome 
  - https://pypi.org/project/Flask-FontAwesome/
- WTForms
  - extension that simplifies form validations 
  - https://wtforms.readthedocs.io/en/3.0.x/
- email_validator
  - extentsion that simplifies email validations 
  - https://pypi.org/project/email-validator/ 
- waitress
  - Waitress is meant to be a production-quality pure Python WSGI server with very acceptable performance
  - https://github.com/Pylons/waitress