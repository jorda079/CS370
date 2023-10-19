from flask import Blueprint, render_template,request, redirect, url_for, g, session
from db_con import get_db_instance, get_db


auth = Blueprint('auth', __name__, static_folder='static', template_folder='templates', url_prefix='')

# sign up for backend
@auth.route("/signup", methods=['GET', 'POST'])
def registration():
    db, cur = get_db_instance()
    # user is not currently logged in
    if 'loggged_in' not in session:
        # data will be available from POST submitted by the form
        if request.method == "POST":
            email = request.form['email']
            # email2 = request.form['email2']
            username = request.form['username']
            password = request.form['password']
            # password2 = request.form['password2']

            # check both email & password already exist
            cur.execute(f"SELECT * from users WHERE email='{email}' AND password=''{password};")
            data = cur.fetchone()
            if data:
                return render_template("error.html")  # duplicated email & password
            else:
                if not data:
                    cur.execute(cur.execute("INSERT INTO users (email, name, password) VALUES (?, ?, ?,)", (email, username, password)))
                    db.commit()
                    db.close()
                return redirect(url_for('login.html'))

    # user is already logged in
    else:
        print("You are alredy logged in.")
    return render_template("index.html")
