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
