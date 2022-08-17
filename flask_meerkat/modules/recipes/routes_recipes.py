
from flask_meerkat import app

from flask import render_template
from flask_login import login_required
from flask_meerkat.modules.recipes.forms_recipes import RecipeForm


@app.route('/recipes', methods=['GET', 'POST'])
@login_required
def recipes():
    return render_template('recipes/recipes.html')


@app.route('/recipe', methods=['GET'])
@login_required
def create_recipe():
    form = RecipeForm()
    return render_template('recipes/upsert_recipe.html', form=form)


@app.route('/recipe', methods=['GET'])
@login_required
def edit_recipe():
    form = RecipeForm()
    return render_template('recipes/upsert_recipe.html', form=form)
