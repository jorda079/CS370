from flask import Flask, render_template, request, redirect, url_for, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt
from auth import auth as auth_blueprint

import sys
import datetime
import bcrypt
import traceback

# ! temporarily except egg.py to avoid error
# from tools.eeg import get_head_band_sensor_object


from db_con import get_db_instance, get_db

from tools.token_required import token_required

#used if you want to store your secrets in the aws valut
#from tools.get_aws_secrets import get_secrets

from tools.logging import logger

ERROR_MSG = "Ooops.. Didn't work!"


# Global custom data type to store username and brainwave data
user_data = {
    # Store current username 
    'username': '',
    # Store brainwave data for each respective movie
    'movie_1_data': [], 
    'movie_2_data': [],
    'movie_3_data': [],
    'movie_4_data': [],
    'movie_5_data': []
}

#Create our app
app = Flask(__name__)
#add in flask json
FlaskJSON(app)

# register auth.py file
app.register_blueprint(auth_blueprint)

#g is flask for a global var storage 
def init_new_env():
    #To connect to DB
    if 'db' not in g:
        g.db = get_db()

    if 'hb' not in g:
        g.hb = get_head_band_sensor_object()

    #g.secrets = get_secrets()
    #g.sms_client = get_sms_client()

#This gets executed by default by the browser if no page is specified
#So.. we redirect to the endpoint we want to load the base page
@app.route('/') #endpoint
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('mainpage.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html')

@app.route("/secure_api/<proc_name>",methods=['GET', 'POST'])
@token_required
def exec_secure_proc(proc_name):
    logger.debug(f"Secure Call to {proc_name}")

    #setup the env
    init_new_env()

    #see if we can execute it..
    resp = ""
    try:
        fn = getattr(__import__('secure_calls.'+proc_name), proc_name)
        resp = fn.handle_request()
    except Exception as err:
        ex_data = str(Exception) + '\n'
        ex_data = ex_data + str(err) + '\n'
        ex_data = ex_data + traceback.format_exc()
        logger.error(ex_data)
        return json_response(status_=500 ,data=ERROR_MSG)

    return resp



@app.route("/open_api/<proc_name>",methods=['GET', 'POST'])
def exec_proc(proc_name):
    logger.debug(f"Call to {proc_name}")

    #setup the env
    init_new_env()

    #see if we can execute it..
    resp = ""
    try:
        fn = getattr(__import__('open_calls.'+proc_name), proc_name)
        resp = fn.handle_request()
    except Exception as err:
        ex_data = str(Exception) + '\n'
        ex_data = ex_data + str(err) + '\n'
        ex_data = ex_data + traceback.format_exc()
        logger.error(ex_data)
        return json_response(status_=500 ,data=ERROR_MSG)

    return resp


if __name__ == '__main__':
    # Debug mode set to true while testing
    app.run(host='0.0.0.0', port=80, debug=True)

