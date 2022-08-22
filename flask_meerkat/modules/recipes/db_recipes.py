from flask_meerkat import db
from flask_meerkat.models import Recipe, Ingredient


def get_recipe_by_id(recipe_id):
    return Recipe.query.get(int(recipe_id))


def insert_recipe(new_recipe, creator_id):
    db.session.add(Recipe(title=new_recipe['title'],
                          ingredients=[Ingredient(name=i['ingredient'], amount=i['amount']) for i in
                                       new_recipe['ingredients']],
                          instruction=new_recipe['instruction'],
                          creator_id=creator_id))
    db.session.commit()


def update_recipe(actual_recipe, new_recipe):
    recipe = Recipe.query.get(int(actual_recipe.id))
    recipe.title = new_recipe['title']
    recipe.ingredients = [Ingredient(name=i['ingredient'], amount=i['amount']) for i in new_recipe['ingredients']]
    db.session.commit()


def find_recipes_by_title(search_string):
    return Recipe.query.filter(Recipe.title.ilike('%{}%'.format(search_string))).limit(25).all()


def delete_recipe(recipe_id):
    recipe = Recipe.query.get(int(recipe_id))
    db.session.delete(recipe)
    db.session.commit()
