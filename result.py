from flask import Blueprint, render_template,request, redirect, url_for, g, session, flash
from db_con import get_db_instance, get_db

res = Blueprint('res', __name__)

# result page
@res.route('/result')
@res.route('/result/<username>')
def result(username=None):
    db, cur = get_db_instance()
    # if user enter result page without login, redirect to login page
    if 'name' not in session:
        flash("You should login first")
        return redirect(url_for("auth.login"))

    username = session['name']

    return render_template('results.html', username=username)