import pickle
import re

# Reads pickle file based on current username.
# Ask the user what pickle file they want to read.
question = "Pickle file to read:\n"
pickle_file = input(question)
pickle_file = "hb_pickled_user_data/" + pickle_file + "_user_data.pickle"

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

    return avg_O1, avg_O2, avg_T3, avg_T4

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

    # Call the function to calculate averages
    movie_1_avg_O1, movie_1_avg_O2, movie_1_avg_T3, movie_1_avg_T4 = calculate_average_user_data(movie_1_read)
    # Print the averages
    print(f'Movie 1 Averages: O1 = {movie_1_avg_O1}, O2 = {movie_1_avg_O2}, T3 = {movie_1_avg_T3}, T4 = {movie_1_avg_T4}\n')

    # Call the function to calculate averages
    movie_2_avg_O1, movie_2_avg_O2, movie_2_avg_T3, movie_2_avg_T4 = calculate_average_user_data(movie_2_read)
    # Print the averages
    print(f'Movie 2 Averages: O1 = {movie_2_avg_O1}, O2 = {movie_2_avg_O2}, T3 = {movie_2_avg_T3}, T4 = {movie_2_avg_T4}\n')

    # Call the function to calculate averages
    movie_3_avg_O1, movie_3_avg_O2, movie_3_avg_T3, movie_3_avg_T4 = calculate_average_user_data(movie_3_read)
    # Print the averages
    print(f'Movie 3 Averages: O1 = {movie_3_avg_O1}, O2 = {movie_3_avg_O2}, T3 = {movie_3_avg_T3}, T4 = {movie_3_avg_T4}\n')

    

# Exception if the file was not found.
except FileNotFoundError:
        print("Error: The file " + pickle_file + " was not found.")

 