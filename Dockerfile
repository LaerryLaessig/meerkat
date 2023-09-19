FROM python:3-slim

ENV MAIL_DEFAULT_SENDER=''
ENV MAIL_PASSWORD=''
ENV MAIL_USERNAME=''
ENV SECRET_KEY=secret_key
ENV SERVER_DOMAIN=''
ENV DATABASE_URI=sqlite:////app/db/meerkat.db

RUN mkdir -p /var/www/meerkat

COPY flask_meerkat /var/www/meerkat/flask_meerkat
COPY app.py /var/www/meerkat
COPY requirements.txt /var/www/meerkat

WORKDIR /var/www/meerkat

RUN mkdir -p /app/db

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]