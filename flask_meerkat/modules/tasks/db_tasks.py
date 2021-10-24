from flask_meerkat import db
from flask_meerkat.models import Task, Subtask, User


def get_all_user():
    return User.query.all()


def insert_task(new_task, creator_id):
    subtasks = []
    for subtask in new_task['subtasks']:
        subtasks.append(Subtask(name=subtask['subtask'], status=subtask['status']))
    task = Task(title=new_task['title'],
                subtasks=subtasks,
                reviser_id=new_task['reviser'],
                creator_id=creator_id)
    db.session.add(task)

    db.session.commit()
