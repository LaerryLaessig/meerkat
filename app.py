#!/usr/bin/env python3
from flask_meerkat import app
from waitress import serve

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
