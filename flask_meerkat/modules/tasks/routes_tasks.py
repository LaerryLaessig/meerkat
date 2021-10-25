from werkzeug.utils import redirect

from flask_meerkat import app

from flask import render_template, request, url_for
from flask_login import login_required, current_user

from flask_meerkat.modules.tasks.db_tasks import insert_task, get_task_by_reviser_id, get_task_by_id, update_task, \
    delete_task, get_task_by_creator_id
from flask_meerkat.database import get_all_user, get_user_by_user_id
from flask_meerkat.modules.tasks.forms_tasks import TaskForm
from flask_meerkat.modules.tasks.mail import send_new_task_mail


@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    task_filter = 'reviser' if request.args.get('filter') is None else request.args.get('filter')
    tasks_to_show = get_task_by_creator_id(current_user.id) if task_filter == 'creator' \
        else get_task_by_reviser_id(current_user.id)
    tasks = [{'title': task.title,
              'id': task.id,
              'subtasks': [{'name': s.name,
                            'status': True if int(s.status) == 1 else False} for s in task.subtasks],
              'reviser': get_user_by_user_id(task.reviser_id).name}
             for task in tasks_to_show]
    return render_template('tasks/tasks.html', tasks=tasks, filter=task_filter)


@app.route('/task', methods=['GET', 'POST'])
@login_required
def create_task():
    form = TaskForm()
    form.reviser.choices = ([(user.id, user.name) for user in get_all_user()])
    if form.new_subtask.data:
        if len(form.subtasks) < 25:
            form.subtasks.append_entry()
    elif form.remove_last_subtask.data:
        if len(form.subtasks) > 0:
            form.subtasks.pop_entry()
    elif request.method == 'POST':
        insert_task(form.data, current_user.id)
        send_new_task_mail(get_user_by_user_id(form.data['reviser']).email)
        return redirect(url_for('tasks'))
    return render_template('tasks/upsert_task.html', form=form)


@app.route('/task/<task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    form = TaskForm()
    form.reviser.choices = [(user.id, user.name) for user in get_all_user()]
    task = get_task_by_id(task_id)
    if request.method == 'GET':
        form.reviser.default = task.reviser_id
        form.process()
        form.title.data = task.title
        selected_reviser = get_user_by_user_id(task.reviser_id)
        form.reviser.default = [selected_reviser.id, selected_reviser.id]
        for s in task.subtasks:
            form.subtasks.append_entry(data={'subtask': s.name, 'status': True if int(s.status) == 1 else False})
        return render_template('tasks/upsert_task.html', form=form, task=task)
    if form.new_subtask.data:
        if len(form.subtasks) < 25:
            form.subtasks.append_entry()
    elif form.remove_last_subtask.data:
        if len(form.subtasks) > 0:
            form.subtasks.pop_entry()
    if form.submit.data:
        update_task(actual_task=task,
                    new_task=form.data)
        return redirect(url_for('tasks'))
    return render_template('tasks/upsert_task.html', form=form, task=task)


@app.route('/task/<task_id>/delete', methods=['POST'])
@login_required
def remove_task(task_id):
    delete_task(task_id)
    return redirect(url_for('tasks', filter=request.args.get('filter')))
