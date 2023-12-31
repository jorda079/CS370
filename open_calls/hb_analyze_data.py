import pickle                          
from auth import request_username
from tools.logging import logger
import time
from db_con import get_db_instance, get_db
from flask import session, redirect, url_for, flash

# Class for brain wave data
class BrainBitSignalData:
    def __init__(self, PackNum, Marker, O1, O2, T3, T4):
        self.PackNum = PackNum
        self.Marker = Marker
        self.O1 = O1
        self.O2 = O2
        self.T3 = T3
        self.T4 = T4

# Function to calculate brain wave averages
def calculate_average_user_data(data_objects_array):
    # Initialize sums and counts for each variable
    sum_O1 = 0
    sum_O2 = 0
    sum_T3 = 0
    sum_T4 = 0
    total_objects = 0

    # Calculate sums
    for data_objects in data_objects_array:
        for obj in data_objects:
            sum_O1 += obj.O1
            sum_O2 += obj.O2
            sum_T3 += obj.T3
            sum_T4 += obj.T4
            total_objects += 1

    # Calculate averages
    avg_O1 = sum_O1 / total_objects
    avg_O2 = sum_O2 / total_objects
    avg_T3 = sum_T3 / total_objects
    avg_T4 = sum_T4 / total_objects
    all_avgs = (avg_O1 + avg_O2 + avg_T3 + avg_T4) / 4

    return avg_O1, avg_O2, avg_T3, avg_T4, all_avgs

# Reads pickle file based on current username.
current_username = request_username()
pickle_file = "hb_pickled_user_data/" + current_username + "_user_data.pickle"
def handle_request():
    # Wait for file to be pickled
    time.sleep(3)

    # We can read the data from the pickle file and analyze it
    try:
        with open(pickle_file, 'rb') as file:
            loaded_user_data = pickle.load(file)
        
        for movie_number, data in loaded_user_data.items():
            if movie_number == 'movie_data':
                movie_read = data  

        # Call the function to calculate averages
        movie_avg_O1, movie_avg_O2, movie_avg_T3, movie_avg_T4, movie_all_avgs = calculate_average_user_data(movie_read)
        # Print the averages
        logger.debug(f'Movie Averages: O1 = {movie_avg_O1}, O2 = {movie_avg_O2}, T3 = {movie_avg_T3}, T4 = {movie_avg_T4}, All Averages = {movie_all_avgs}\n')

        db, cur = get_db_instance()
        if 'id' in session:
            user_id = session['id']
            cur.execute("UPDATE users SET hb=(?) WHERE id=(?)", (movie_all_avgs, user_id)) 
            db.commit()
            db.close()        

        # Return that data was analyzed
        return ["Analyzed Brainwave Data"]
    
    # Exception if the file was not found.
    except FileNotFoundError:
            logger.debug("Error: The file " + pickle_file + " was not found.")
            return ["Failed To Read File"]     
 