from flask_meerkat import db
from flask_meerkat.models import Recipe


def get_recipe_by_id(recipe_id):
    return Recipe.query.get(int(recipe_id))
