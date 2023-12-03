from flask import request, g                                   
from tools.logging import logger   
from neurosdk.cmn_types import * 
from app import user_data
import copy
from auth import request_username

# Creates user_data template
recorded_user_data = copy.deepcopy(user_data)

# Stores all the recorded user data from each movie
def handle_request():
    # Get username from current session, store it in the object
    recorded_user_data['cur_username'] = request_username()
    
    # Stores filler data if headband not connected.
    if g.hb == None:
        recorded_user_data['movie_1_data'] = ['1111', '11', '1']
        logger.debug("Finished Movie 1")
        recorded_user_data['movie_2_data'] = ['2222', '2', '2']
        logger.debug("Finished Movie 2")
        recorded_user_data['movie_3_data'] = ['3333', '3', '3']
        logger.debug("Finished Movie 3")
        logger.debug("Finished Test Recording")
        return ["Finished Recording Test"]
    
    # Record headband data
    # Store values for each movie
    else:
        # * Store recorded data here *
        logger.debug("Finished Recording")
        return ["Finished Recording"]
