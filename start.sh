#!/usr/bin/env bash

echo "activate virtual venv"
. venv/bin/activate

echo "set admin user and pw"
export SECRET_KEY='secret_key'
export MAIL_USERNAME=''
export MAIL_PASSWORD=''
export MAIL_DEFAULT_SENDER=''
export SERVER_DOMAIN=''
export DATABASE_URI='sqlite:///meerkat.db'

echo 'start server'
python app.py

echo "deactivate venv"
deactivate
