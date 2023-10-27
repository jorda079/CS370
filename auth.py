from flask import Blueprint, render_template,request, redirect, url_for, g, session, flash
from db_con import get_db_instance, get_db

auth = Blueprint('auth', __name__)

# user authentication: sign-up
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

# code to validate and add user to database goes here
@auth.route('/signup', methods=['GET', 'POST'])
def signup_post():
    db, cur = get_db_instance()
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    question1 = request.form.get('question1')
    question2 = request.form.get('question2')
    question3 = request.form.get('question3')
    message = request.form.get("message")    

    cur.execute("SELECT email FROM users WHERE email=(?)", email)
    user = cur.fetchone()
    # if returns a user, then the email already exists in database
    if user:
        flash("Email address already exists")
        return redirect(url_for('auth.signup'))
    
    # add the new user to the database
    cur.execute("INSERT INTO users (email, username, password) VALUES (?, ?, ?)", (email, username, password))
    
    # add the new questionnaire data to the database
    cur.execute("INSERT INTO questionnaire (answer_1, answer_2, answer_3, comments) VALUES (?, ?, ?, ?)",(question1, question2, question3, message))
    db.commit()
    db.close()
    return redirect(url_for('auth.login'))    
    

# user authentication: login method
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

# login code goes here
@auth.route('/login', methods=['GET', 'POST'])
def login_post():
    db, cur = get_db_instance()
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    cur.execute("SELECT username FROM users WHERE username=(?)", username)
    user = cur.fetchone()

    # check if the user actaully exsits
    if not user or user[1] != password:
        flash("Please check your login details and try again.")
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    return redirect(url_for("auth.profile"))

# user authentication: user profile mtethod
@auth.route('/profile', methods=['GET', 'POST'])
def profile():
    db, cur = get_db_instance()
    return render_template("profile.html")

@auth.route('/logout')
# Requests current username
def request_username():
    #db, cur = get_db_instance()

    return "test_username"
    
    # Need to request current username from database. 
    # We can make a global variable to store the user_id
    # while they are logged in. Then request info from 
    # database referencing the user_id.
