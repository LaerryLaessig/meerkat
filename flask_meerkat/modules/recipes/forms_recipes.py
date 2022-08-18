from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, TextAreaField
from wtforms.validators import DataRequired


class IngredientForm(FlaskForm):
    ingredient = StringField('Ingredient', validators=[DataRequired()])
    amount = StringField('Amount')


class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    ingredients = FieldList(FormField(IngredientForm), min_entries=0, max_entries=25)
    instruction = TextAreaField('Instruction', validators=[DataRequired()])
    new_ingredient = SubmitField('+', render_kw={'formnovalidate': True})
    remove_last_ingredient = SubmitField('-',  render_kw={'formnovalidate': True})
    submit = SubmitField('Save', render_kw={'novalidate': True})


class SearchRecipesForm(FlaskForm):
    searchword = StringField('Searchword', validators=[DataRequired()])
    submit = SubmitField('Search', render_kw={'novalidate': True})


