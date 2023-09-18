from werkzeug.utils import redirect

from flask_meerkat import app

from flask import render_template, request, url_for
from flask_login import login_required, current_user

from flask_meerkat.models import Task, Subtask
from flask_meerkat.modules.recipes.db_recipes import get_recipe_by_id
from flask_meerkat.modules.tasks.db_tasks import insert_task, get_task_by_reviser_id, get_task_by_id, update_task, \
    delete_task, get_task_by_creator_id
from flask_meerkat.database import get_all_user, get_user_by_user_id, get_username_by_user_id, get_user_email_by_user_id
from flask_meerkat.modules.tasks.forms_tasks import TaskForm
from flask_meerkat.modules.tasks.mail import send_new_task_mail


@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    task_filter = 'reviser' if request.args.get('filter') is None else request.args.get('filter')
    return render_template('tasks/tasks.html', tasks=create_form_value(task_filter), filter=task_filter)


@app.route('/task', methods=['GET', 'POST'])
@login_required
def create_task():
    form = create_task_form()
    if request.args.get('recipe_id') is not None:
        recipe_id = request.args['recipe_id']
        recipe = get_recipe_by_id(recipe_id)
        task = Task(title=recipe.title,
                    reviser_id=current_user.id,
                    subtasks=[Subtask(name=f'{i.amount} {i.name}', status=0) for i in recipe.ingredients],
                    creator_id=current_user.id)
        set_values(form, task)
        return render_template('tasks/upsert_task.html', form=form)
    else:
        action_subtasks(form=form)
        if got_submit_data(form):
            insert_task(form.data, current_user.id)
            send_new_task_mail(get_user_email_by_user_id(form.data['reviser']), form.data)
            return redirect_to_tasks()
        return render_template('tasks/upsert_task.html', form=form)


@app.route('/task/<task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    form = create_task_form()
    task = get_task_by_id(task_id)
    if is_request_GET(request):
        if is_current_user_not_creator_and_not_reviser(task):
            return redirect_to_tasks()
        set_values(form, task)
        return render_upsert_task_with_form_task(form, task)
    action_subtasks(form=form)
    if got_submit_data(form):
        update_task(actual_task=task, new_task=form.data)
        return redirect_to_tasks()
    return render_upsert_task_with_form_task(form, task)


@app.route('/task/<task_id>/delete', methods=['POST'])
@login_required
def remove_task(task_id):
    delete_task(task_id)
    return redirect(url_for('tasks', filter=request.args.get('filter')))


def redirect_to_tasks():
    return redirect(url_for('tasks'))


def get_tasks_to_show(task_filter):
    return get_task_by_creator_id(current_user.id) if task_filter == 'creator' \
        else get_task_by_reviser_id(current_user.id)


def render_upsert_task_with_form_task(form, task):
    return render_template('tasks/upsert_task.html', form=form, task=task)


def got_submit_data(form):
    return form.submit.data


def is_request_method(req, method):
    return req.method == method


def is_request_GET(req):
    return is_request_method(req, 'GET')


def is_request_POST(req):
    return is_request_method(req, 'POST')


def create_task_form():
    form = TaskForm()
    form.reviser.choices = get_user_to_choices()
    return form


def int_to_boolean(i):
    return True if i == 1 else False


def get_user_to_choices():
    return [(user.id, user.name) for user in get_all_user()]


def is_current_user_not_creator_and_not_reviser(task):
    return current_user.id != task.creator_id and current_user.id != task.reviser_id


def set_values(form, task):
    form.reviser.default = task.reviser_id
    form.process()
    form.title.data = task.title
    selected_reviser = get_user_by_user_id(task.reviser_id)
    form.reviser.default = [selected_reviser.id, selected_reviser.id]
    set_subtasks(form, task)


def set_subtasks(form, task):
    for s in task.subtasks:
        form.subtasks.append_entry(data={'subtask': s.name, 'status': int_to_boolean(int(s.status))})


def create_form_value(task_filter):
    return [{'title': task.title,
             'id': task.id,
             'subtasks': [{'name': s.name,
                           'status': int_to_boolean(int(s.status))} for s in task.subtasks],
             'reviser': get_username_by_user_id(task.reviser_id),
             'creator': get_username_by_user_id(task.creator_id)}
            for task in get_tasks_to_show(task_filter)]


def action_subtasks(form):
    if form.new_subtask.data:
        if len(form.subtasks) < 25:
            form.subtasks.append_entry()
    elif form.remove_last_subtask.data:
        if len(form.subtasks) > 0:
            form.subtasks.pop_entry()
