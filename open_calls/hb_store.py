from flask import request, g                                                                 
from tools.logging import logger   
from neurosdk.cmn_types import * 
import pickle
from app import user_data
from open_calls.hb_record import recorded_movie_1_data, recorded_movie_2_data, recorded_movie_3_data, recorded_movie_4_data, recorded_movie_5_data
from auth import request_username

# Creates user_data template
recorded_user_data = user_data.copy

# Get username from database, store it user_data in object
recorded_user_data['username'] = request_username()

# Stores all the recorded user data from each movie
recorded_user_data['movie_1_data'] = recorded_movie_1_data
recorded_user_data['movie_2_data'] = recorded_movie_2_data
recorded_user_data['movie_3_data'] = recorded_movie_3_data
recorded_user_data['movie_4_data'] = recorded_movie_4_data
recorded_user_data['movie_5_data'] = recorded_movie_5_data

# Then we pickle the data in a file created for that indiviual user
