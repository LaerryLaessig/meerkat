from flask_meerkat import app

from flask import render_template
from flask_login import login_required


@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    return render_template('tasks/tasks.html')
