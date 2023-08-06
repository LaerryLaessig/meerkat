FROM python:3-slim

COPY flask_meerkat /var/www/meerkat
COPY app.py /var/www/meerkat
COPY requirements.txt /var/www/meerkat

WORKDIR /var/www/meerkat

RUN mkdir -p /app/db

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
