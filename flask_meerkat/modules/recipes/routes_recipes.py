
from flask_meerkat import app

from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user

from flask_meerkat.database import get_username_by_user_id
from flask_meerkat.modules.recipes.damig_recipes import do_damig
from flask_meerkat.modules.recipes.db_recipes import get_recipe_by_id, insert_recipe, find_recipes_by_title, \
    update_recipe, delete_recipe
from flask_meerkat.modules.recipes.forms_recipes import RecipeForm, SearchRecipesForm


def action_ingredients(form):
    if form.new_ingredient.data:
        if len(form.ingredients) < 25:
            form.ingredients.append_entry()
    elif form.remove_last_ingredient.data:
        if len(form.ingredients) > 0:
            form.ingredients.pop_entry()


@app.route('/recipes', methods=['GET', 'POST'])
@login_required
def recipes():
    return render_template('recipes/recipes.html', form=SearchRecipesForm())


@app.route('/recipe', methods=['GET', 'POST'])
@login_required
def create_recipe():
    form = RecipeForm()
    action_ingredients(form=form)
    if got_submit_data(form):
        insert_recipe(form.data, current_user.id)
        return redirect(url_for('recipes'))
    return render_template('recipes/upsert_recipe.html', form=form)


@app.route('/search_recipes', methods=['GET'])
@login_required
def search_recipes():
    return render_template('recipes/recipes.html',
                           form=SearchRecipesForm(),
                           recipes=[{'id': r.id,
                                     'title': r.title,
                                     'ingredients': r.ingredients,
                                     'creator': get_username_by_user_id(r.creator_id)}
                                    for r in find_recipes_by_title(request.args['searchstring'])])


@app.route('/recipe/<recipe_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    form = RecipeForm()
    recipe = get_recipe_by_id(recipe_id)
    if is_request_GET(request):
        set_values(form, recipe)
        return render_template('recipes/upsert_recipe.html', form=form, recipe=recipe)
    action_ingredients(form=form)
    if got_submit_data(form):
        update_recipe(actual_recipe=recipe, new_recipe=form.data)
        return redirect(url_for('recipes'))
    return render_template('recipes/upsert_recipe.html', form=form, recipe=recipe)


@app.route('/recipe/<recipe_id>/delete', methods=['POST'])
@login_required
def remove_recipe(recipe_id):
    delete_recipe(recipe_id)
    return redirect(url_for('recipes'))


@app.route('/recipe/damig', methods=['GET'])
def damig():
    do_damig()
    return 'done'


def got_submit_data(form):
    return form.submit.data


def is_request_method(req, method):
    return req.method == method


def is_request_GET(req):
    return is_request_method(req, 'GET')


def set_values(form, recipe):
    form.title.data = recipe.title
    form.instruction.data = recipe.instruction
    set_ingredients(form, recipe)


def set_ingredients(form, recipe):
    for ingredient in recipe.ingredients:
        form.ingredients.append_entry(data={'ingredient': ingredient.name, 'amount': ingredient.amount})
