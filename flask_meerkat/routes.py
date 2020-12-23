from flask import render_template
from flask_meerkat import app


@app.route('/', methods=['GET'])
def first_page():
    return render_template('index.html')


@app.route('/health')
def health_check():
    return {"status": "ok"}
