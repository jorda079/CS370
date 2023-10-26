from flask import Blueprint, render_template,request, redirect, url_for, g, session
from db_con import get_db_instance, get_db


auth = Blueprint('auth', __name__, static_folder='static', template_folder='templates', url_prefix='')

# user authentication: sign-up
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
            question1 = request.form['question1']
            question2 = request.form['question2']
            question3 = request.form['question3']
            message = request.form['message']
            # password2 = request.form['password2']

            # check both email & password already exist
            cur.execute(f"SELECT * from users WHERE email='{email}' AND password=''{password};")
            data = cur.fetchone()
            if data:
                return render_template("error.html")  # duplicated email & password
            else:
                if not data:
                    cur.execute("INSERT INTO users (email, name, password) VALUES (?, ?, ?)", (email, username, password))
                    cur.execute("INSERT INTO questionnaire (answer_1, answer_2, answer_3, comments) VALUES (?, ?, ?, ?)", (question1, question2, question3, message))
                    db.commit()
                    db.close()
                return redirect(url_for('login.html'))

    # user is already logged in
    else:
        print("You are alredy logged in.")
        return redirect(url_for('index.html'))
    return render_template("/static/signup.html")

# user authentication: login
@auth.route("/login", methods=['GET', 'POST'])
def login():
    db, cur = get_db_instance()
    render_template("/static/login.html")

# user authentication: user profile
@auth.route("/profile", methods=['GET', 'POST'])
def profile():
    db, cur = get_db_instance()
    render_template("/static/profile.html")

# Requests current username
def request_username():
    #db, cur = get_db_instance()

    return "test_username"
    
    # Need to request current username from database. 
    # We can make a global variable to store the user_id
    # while they are logged in. Then request info from 
    # database referencing the user_id.
