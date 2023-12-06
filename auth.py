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
    gender = request.form.get('gender')
    birthdate = request.form.get('birthdate')
    address = request.form.get('address')
    phone = request.form.get('phone')
    introduce = request.form.get('introduce')
    question1 = request.form.get('question1')
    question2 = request.form.get('question2')
    question3 = request.form.get('question3')
    message = request.form.get("message")    


    # find the user in local database with input 
    cur.execute("SELECT * FROM users WHERE email=(?)", [email])
    user = cur.fetchone()
    if user:
        flash("Email already exists, please use different email.")
        return redirect(url_for('auth.signup', username=session['name']))
    
    # add new user into database with questionnarie answer
    # save database using commit()
    cur.execute("INSERT INTO users (name, password, email, address, phone, gender, birth, introduce) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (username, password, email, address, phone, gender, str(birthdate), introduce))
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
    # get input from html files
    email = request.form.get('email')
    password = request.form.get('password')
    # remember = True if request.form.get('remember') else False

    # find the user in local database with input 
    cur.execute("SELECT * FROM users WHERE email=(?)", [email])
    user = cur.fetchone()

    # check if the user actaully exsits & check password
    if not user or str(password) != user[2]:
        flash("Please check your login details and try again.")
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    # session includes user name & id
    session['name'] = user[1]   
    session['id'] = user[0]
    db.close()
    return redirect(url_for("auth.profile", username=session['name']))

# user authentication: user profile mtethod
@auth.route('/profile/')
@auth.route('/profile/<username>')
def profile(username=None):
    db, cur = get_db_instance()
    # if user enter profile without login, redirect to login page
    if 'name' not in session:
        flash("You should login first")
        return redirect(url_for("auth.login"))
    
    # call user information to profile 
    username = session['name']
    cur.execute("SELECT * FROM users WHERE name=(?)", [username])
    user = cur.fetchone()
    profile={
    'name': user[1],
    'email': user[3],
    'address': user[4],
    'phone': user[5],
    'gender':user[6],
    'birth': user[7],
    'introduce': user[8],
    'profile_pic' : user[9]
    }
    db.close()
    return render_template("profile.html", profile=profile, username=username)

# user authentication: logout method
@auth.route('/logout')
def logout():
    # clear session & logout re-direct to main page
    session.pop('name', None)
    return redirect(url_for('main'))


# Requests current username
@auth.route('/index')
def request_username():
    # If the user name exists we return the name.
    if 'name' in session:
        return session['name']
    # Otherwise we return a test username.
    return "test_username"
