from flask import request, g                                                                 
from tools.logging import logger   
from neurosdk.cmn_types import * 

# Array to store brainwave data from headband
# Variable for each respective movie
recorded_movie_1_data = []
recorded_movie_2_data = []
recorded_movie_3_data = []
recorded_movie_4_data = []
recorded_movie_5_data = []

# Record headband data
# Store values for each movie
