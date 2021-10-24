from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, BooleanField, SelectField
from wtforms.validators import DataRequired


class SubTaskForm(FlaskForm):
    subtask = StringField('Subtask', validators=[DataRequired()])
    status = BooleanField('Status')


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    reviser = SelectField('Reviser')
    subtasks = FieldList(FormField(SubTaskForm), min_entries=1, max_entries=25)
    new_subtask = SubmitField('+', render_kw={'formnovalidate': True})
    remove_last_subtask = SubmitField('-',  render_kw={'formnovalidate': True})
    submit = SubmitField('Save')



