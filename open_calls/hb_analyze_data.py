import pickle
from flask import request, g                                   
from neurosdk.cmn_types import * 
from auth import request_username
from tools.logging import logger

# Reads pickle file based on current username.
current_username = request_username()
pickle_file = "hb_pickled_user_data/" + current_username + ".pickle"

# We can read the data from the pickle file and analyze it
try:
    with open(pickle_file, 'rb') as file:
        loaded_user_data = pickle.load(file)
    
    for movie_number, data in loaded_user_data.items():
        if movie_number == 'movie_1_data':
          movie_1_read = data  
        elif movie_number == 'movie_2_data':
            movie_2_read = data  
        elif movie_number == 'movie_3_data':
            movie_3_read = data 

    logger.debug("Movie 1: " + str(movie_1_read))
    logger.debug("Movie 2: " + str(movie_2_read))
    logger.debug("Movie 3: " + str(movie_3_read))

    # * Analyze Data here *

#Exception if the file was not found.
except FileNotFoundError:
        logger.debug("Error: The file " + pickle_file + " was not found.")     
 