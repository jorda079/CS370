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
    # Store brainwave data for each respective movie
    'movie_1_data': [], 
    'movie_2_data': [],
    'movie_3_data': []
}

# Creates user_data template
recorded_user_data = copy.deepcopy(user_data)

# Stores the value for the current movie
current_movie = 0

# Update the value of current movie to passed value
def update_current_movie(data):
    global current_movie
    current_movie = data

# Appends data to user data structure
def update_user_data(data):
    global recorded_user_data

    # Iterate for all possible movie values and store respectively
    if(current_movie == 1):
        recorded_user_data['movie_1_data'].append(data)
    elif(current_movie == 2):
        recorded_user_data['movie_2_data'].append(data)
    elif(current_movie == 3):
        recorded_user_data['movie_3_data'].append(data)

# Stores all the recorded user data from each movie
def handle_request():
    # Get username from current session, store it in the object
    recorded_user_data['cur_username'] = request_username()
    
    # Stores filler data if headband not connected.
    if g.hb == None:

        # Movie value 4 means all videos have been watched
        # So exit loop at 4
        while(current_movie != 4):

            # Iterate for all possible movie values and store respectively
            if(current_movie == 0):
                # No movie has been selected
                logger.debug("Invalid Movie")

            elif(current_movie == 1):
                # If empty fill with test data
                if(recorded_user_data['movie_1_data'] == []):
                    update_user_data('1111')
                    update_user_data('11')
                    update_user_data('1')
                    logger.debug("Finished Movie 1")

            elif(current_movie == 2):
                # If empty fill with test data
                if(recorded_user_data['movie_2_data'] == []):
                    update_user_data('2222')
                    update_user_data('2')
                    update_user_data('2')
                    logger.debug("Finished Movie 2")

            elif(current_movie == 3):
                # If empty fill with test data
                if(recorded_user_data['movie_3_data'] == []):
                    update_user_data('3333')
                    update_user_data('3')
                    update_user_data('3')
                    logger.debug("Finished Movie 3")
            
            # Sleep for time between choosing videos
            time.sleep(1)
        
        # Data recorded so return
        logger.debug("Finished Test Recording")
        return ["Finished Recording Test"]
    
    # Stores head band data
    else:
        # Iterate, checking for final movie value
        while(current_movie != 4):
            # Sleep for time between choosing videos
            time.sleep(1)

        # Data has been recorded so return
        logger.debug("Finished Recording")
        return ["Finished Recording"]
    
