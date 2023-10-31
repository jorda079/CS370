from flask import Blueprint, render_template,request, redirect, url_for, g, session, flash
from db_con import get_db_instance, get_db

auth = Blueprint('auth', __name__)

# user authentication: sign-up
@auth.route('/signup')
def signup():
    if 'name' in session:
        return redirect(url_for("auth.profile", username=session['name']))
    return render_template('signup.html')

# code to validate and add user to database goes here
@auth.route('/signup', methods=['POST'])
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
        return redirect(url_for('auth.signup', username=session['name']))
    
    # add the new user to the database
    cur.execute("INSERT INTO users (email, name, password) VALUES (?, ?, ?)", (email, username, password))
    
    # add the new questionnaire data to the database
    cur.execute("INSERT INTO questionnaire (answer_1, answer_2, answer_3, comments) VALUES (?, ?, ?, ?)",(question1, question2, question3, message))
    db.commit()
    db.close()
    return redirect(url_for('auth.login'))    
    

# user authentication: login method
@auth.route('/login')
def login():
    if 'name' in session:
        return redirect(url_for("auth.profile", username=session['name']))
    return render_template("login.html")

# login code goes here
@auth.route('/login', methods=['POST'])
def login_post():
    db, cur = get_db_instance()
    username = request.form.get('username')
    password = request.form.get('password')
    # remember = True if request.form.get('remember') else False

    cur.execute("SELECT * FROM users WHERE name=(?)", username)
    user = cur.fetchone()

    # check if the user actaully exsits & check password
    if not user or str(password) != user[2]:
        # flash("Please check your login details and try again.")
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    session['name'] = user[1]   # put username in to session 
    return redirect(url_for("auth.profile", username=session['name']))

# user authentication: user profile mtethod
@auth.route('/profile', methods=['GET', 'POST'])
def profile():
    db, cur = get_db_instance()
    if 'name' not in session:
        flash("You should login first")
        return redirect(url_for("auth.login"))
    
    username = session['name']
    cur.execute("SELECT * FROM users WHERE name=(?)", username)
    user = cur.fetchone()
    profile={
    'name': user[1],
    'email': user[3],
    'address': user[4],
    'phone': user[5],
    'gender':user[6],
    'birth': user[7],
    'introduce': user[8]
    }

    return render_template("profile.html", profile=profile)

# # check user already logged in
# @auth.before_request
# def check_loggedin():
#     if 'id' in session:   # if user alreday logged in, send them to profile 
#         return redirect(url_for("auth.profile"))

@auth.route('/logout')
def logout():
    # clear session & logout re-direct to main page
    session.pop('name', None)
    return redirect(url_for('main'))


# Requests current username
def request_username():
    #db, cur = get_db_instance()
    return session['username']
    
    # Need to request current username from database. 
    # We can make a global variable to store the user_id
    # while they are logged in. Then request info from 
    # database referencing the user_id.
