from flask import render_template, request, url_for
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from flask_meerkat import app
from flask_meerkat.database import \
    find_whitelist, insert_whitlist_email, \
    delete_whitelist_by_id
from flask_meerkat.modules.admin.forms_admin import AddWhiteListForm


@app.route('/whitelist', methods=['GET', 'POST'])
@login_required
def whitelist():
    if current_user.id == 1:
        form = AddWhiteListForm()
        if request.method == 'GET':
            emails = find_whitelist()
            return render_template('admin/whitelist.html', form=form, emails=emails)
        elif request.method == 'POST' and form.validate_on_submit:
            insert_whitlist_email(form.email.data)
            return redirect(url_for('whitelist'))
    else:
        return redirect(url_for('home'))


@app.route('/whitelist/<whitelist_id>/delete', methods=['POST'])
def remove_whitelist_mail(whitelist_id):
    if current_user.id == 1:
        delete_whitelist_by_id(whitelist_id)
        return redirect(url_for('whitelist'))
    else:
        return redirect(url_for('home'))


@app.route('/health', methods=['GET'])
def get_health():
    return {'status': 'ok'}
