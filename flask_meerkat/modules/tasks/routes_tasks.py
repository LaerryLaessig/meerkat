from flask_meerkat import app

from flask import render_template
from flask_login import login_required

from flask_meerkat.modules.tasks.forms_tasks import TaskForm


@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():

    return render_template('tasks/tasks.html')


@app.route('/task', methods=['GET', 'POST'])
@login_required
def create_task():
    form = TaskForm()
    if form.new_subtask.data:
        form.subtasks.append_entry()
    if form.remove_last_subtask.data:
        form.subtasks.pop_entry()
    return render_template('tasks/upsert_task.html', form=form)
