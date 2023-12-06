from flask import g                         
from tools.logging import logger   
from neurosdk.cmn_types import * 
import copy
from auth import request_username
import time

# Custom data type to store username and brainwave data
user_data = {
    # Store current username 
    'cur_username': "",
    # Store brainwave data for the movies
    'movie_data': [], 
}

# Creates user_data template
recorded_user_data = copy.deepcopy(user_data)

# Stores the value for movies status
movie_finished = False

# Update the value of current movie to passed value
def update_movie_status(data):
    global movie_finished
    movie_finished = data

# Appends data to user data structure
def update_user_data(data):
    global recorded_user_data

    # Appends brain wave data to array
    recorded_user_data['movie_data'].append(data)

# Stores all the recorded user data from the movies
def handle_request():
    # Get username from current session, store it in the object
    recorded_user_data['cur_username'] = request_username()
    
    # Stores filler data if headband not connected.
    if g.hb == None:

        update_user_data('1111')
        update_user_data('11')
        update_user_data('1')

        update_user_data('2222')
        update_user_data('2')
        update_user_data('2')

        update_user_data('3333')
        update_user_data('3')
        update_user_data('3')

        # Loop while videos are being watched
        while(movie_finished == False):
            # Sleep for time between checking value
            time.sleep(1)
        
        # Data recorded so return
        logger.debug("Finished Test Recording")
        return ["Finished Recording Test"]
    
    # Stores head band data
    else:
        # Iterate, checking for final movie value
        while(movie_finished == False):
            # Sleep for time between choosing videos
            time.sleep(1)

        # Data has been recorded so return
        logger.debug("Finished Recording")
        return ["Finished Recording"]
    
