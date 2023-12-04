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
    
    # matching process algorithms
    user_id = session['id']
    cur.execute("SELECT * FROM questionnaire WHERE _id=(?)", [user_id])
    current_user = cur.fetchone()
    
    cur.execute("SELECT _id FROM questionnaire WHERE answer_1=(?) AND answer_2=(?) AND answer_3=(?)", (current_user[1], current_user[2], current_user[3]))
    match_users = cur.fetchall()

    print(match_users)

    rows = []

    for user in match_users:
        cur.execute("SELECT * FROM users WHERE id=(?)", user)
        rows.append(cur)
        
    return render_template('results.html', username=username, rows=rows)