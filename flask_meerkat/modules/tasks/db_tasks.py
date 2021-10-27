from flask_meerkat import db
from flask_meerkat.models import Task, Subtask


def get_task_by_id(task_id):
    return Task.query.get(int(task_id))


def insert_task(new_task, creator_id):
    db.session.add(Task(title=new_task['title'],
                        subtasks=[Subtask(name=s['subtask'], status=s['status']) for s in new_task['subtasks']],
                        reviser_id=new_task['reviser'],
                        creator_id=creator_id))
    db.session.commit()


def update_task(actual_task, new_task):
    task = Task.query.get(int(actual_task.id))
    task.title = new_task['title']
    task.reviser_id = new_task['reviser']
    task.subtasks = [Subtask(name=s['subtask'], status=s['status']) for s in new_task['subtasks']]
    db.session.commit()


def delete_task(task_id):
    task = Task.query.get(int(task_id))
    db.session.delete(task)
    db.session.commit()


def get_task_by_reviser_id(reviser_id):
    return Task.query.filter_by(reviser_id=int(reviser_id)).all()


def get_task_by_creator_id(creator_id):
    return Task.query.filter_by(creator_id=int(creator_id)).all()
