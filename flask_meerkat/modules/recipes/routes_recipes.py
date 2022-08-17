from werkzeug.utils import redirect

from flask_meerkat import app

from flask import render_template
from flask_login import login_required


@app.route('/recipes', methods=['GET', 'POST'])
@login_required
def recipes():

    return render_template('recipes/recipes.html')