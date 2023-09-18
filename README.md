# Simple Blog and Task Management System

This is a Python Flask project that provides a platform for creating and managing blog posts, recipes, and tasks for different users.

## Features

### User Sign Up and Authentication

- Only whitelisted users can sign up.
- The first user to sign up is automatically added to the whitelist and becomes the admin.

### Whitelist Management

- The admin has the authority to manage the whitelist, controlling who can sign up.

### Blog Posts

- All registered users can create and manage their own blog posts.

### Tasks

- All registered users can create tasks.
- Users can view and edit tasks if they are the creator or reviser of the task.

### Recipes

- All registered users can search and create recipes.
- Users can create tasks based on a recipe's list of ingredients.

### Account Management

- Users can edit their usernames and email addresses.

## Environment Variables

To run the application, you need to set the following environment variables:

- `SECRET_KEY`: Change this in the `start.sh` script or set it as an environment variable. Default value is `secret_key`.
- `MAIL_USERNAME`: Change this in the `start.sh` script or set it as an environment variable. Used for password reset and task notifications. Default value is an empty string.
- `MAIL_PASSWORD`: Change this in the `start.sh` script or set it as an environment variable. Default value is an empty string.
- `MAIL_DEFAULT_SENDER`: Change this in the `start.sh` script or set it as an environment variable. Used as the sender's email address for password reset and task notifications. Default value is an empty string.

## Dependencies

This project relies on the following dependencies:

- [Flask](https://palletsprojects.com/p/flask/): Micro web framework.
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/): Provides bcrypt hashing utilities.
- [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/): Simplifies HTTP authentication with Flask routes.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/): Simplifies using SQLAlchemy.
- [Flask-Bootstrap](https://github.com/mbr/flask-bootstrap): Simplifies using Bootstrap 4.
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/): Simplifies user session management.
- [Flask-Mailer](https://pythonhosted.org/Flask-Mail/): Simplifies sending emails to users.
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/latest/): Integrates Flask with WTForms, including CSRF, file upload, and reCAPTCHA.
- [Flask-FontAwesome](https://pypi.org/project/Flask-FontAwesome/): Simplifies using FontAwesome icons.
- [WTForms](https://wtforms.readthedocs.io/en/3.0.x/): Simplifies form validations.
- [email_validator](https://pypi.org/project/email-validator/): Simplifies email validations.
- [Waitress](https://github.com/Pylons/waitress): A production-quality pure Python WSGI server with good performance.

## Usage

1. Set the required environment variables as mentioned above.
2. Run the `start.sh` script to start the application.
3. Access the application in your web browser.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.