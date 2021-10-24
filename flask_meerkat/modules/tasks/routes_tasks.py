from werkzeug.utils import redirect

from flask_meerkat import app

from flask import render_template, request, url_for
from flask_login import login_required, current_user

from flask_meerkat.modules.tasks.db_tasks import insert_task, get_all_user
from flask_meerkat.modules.tasks.forms_tasks import TaskForm


@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():

    return render_template('tasks/tasks.html')


@app.route('/task', methods=['GET', 'POST'])
@login_required
def create_task():
    form = TaskForm()
    form.reviser.choices = ([(user.id, user.name) for user in get_all_user()])
    if form.new_subtask.data:
        form.subtasks.append_entry()
    elif form.remove_last_subtask.data:
        form.subtasks.pop_entry()
    elif request.method == 'POST':
        insert_task(form.data, current_user.id)
        return redirect(url_for('tasks'))
    return render_template('tasks/upsert_task.html', form=form)
