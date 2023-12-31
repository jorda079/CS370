from flask import Blueprint, render_template,request, redirect, url_for, g, session, flash
from db_con import get_db_instance, get_db

res = Blueprint('res', __name__)


def hb_upload():

    return

# result page
@res.route('/result')
@res.route('/result/<username>')
def result(username=None):
    db, cur = get_db_instance()
    # if user enter result page without login, redirect to login page
    if 'name' not in session:
        flash("You should login first")
        return redirect(url_for("auth.login"))
    
    '''
    * matching process method
    * algorithms: match with the person who has the same answer from questionnaire
    '''
    user_id = session['id']
    cur.execute("SELECT * FROM questionnaire WHERE _id=(?)", [user_id])
    current_user = cur.fetchone()
    
    cur.execute("SELECT _id FROM questionnaire WHERE group_num =(?) AND _id != (?)", (current_user[1], user_id))
    matched_users = cur.fetchall()

    users = []

    # each row: the group of people who have same questionnaire answer
    for user in matched_users:
        cur.execute("SELECT * FROM users WHERE id=(?)", user)
        row = cur.fetchone()
        users.append(row)
    db.close()
    return render_template('results.html', username=username, users=users)