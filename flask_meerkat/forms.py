from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_meerkat import bcrypt
from flask_login import current_user
from flask_meerkat.database import find_user_by_mail, find_user_by_username


def check_password(form, field):
    user = find_user_by_mail(form.email.data)
    if user is None or not bcrypt.check_password_hash(user.password, field.data):
        raise ValidationError('Username or password is incorrect')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=2,
                                                          max=24,
                                                          message='Username must be between 2 and 24 characters long')])
    email = StringField('Email', validators=[DataRequired(),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(),
                                                                     EqualTo('password',
                                                                             message='Field password and field confirm \
                                                                             password must match')])
    submit = SubmitField('Sign up')

    def validate_email(self, email):
        if find_user_by_mail(email.data) is not None:
            raise ValidationError('Email adress already exists')

    def validate_username(self, username):
        if find_user_by_username(username.data) is not None:
            raise ValidationError('Username already exists')


class SignInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     check_password])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class AccountForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    submit = SubmitField('Update')

    def validate_email(self, email):
        if find_user_by_mail(email.data) is not None and current_user.email != email.data:
            raise ValidationError('Email adress already exists')

    def validate_username(self, username):
        if find_user_by_username(username.data) is not None and current_user.name != username.data:
            raise ValidationError('Username already exists')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send')

    def validate_email(self, email):
        if find_user_by_mail(email.data) is None:
            raise ValidationError('Unknown email adress')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(),
                                                                     EqualTo('password',
                                                                             message='Field password and field confirm \
                                                                                password must match')])
    submit = SubmitField('Change')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Post')
