import pickle

# Ask the user what pickle file they want to read.
question = "Pickle file to read:\n"
pickle_file = input(question)
pickle_file = "hb_pickled_user_data/" + pickle_file + ".pickle"

# We can read the data from the pickle file and print it.
try:
    with open(pickle_file, 'rb') as file:
        loaded_user_data = pickle.load(file)

    # Collects movie data from loaded variable
    for movie_number, data in loaded_user_data.items():
        if movie_number == 'movie_1_data':
          movie_1_read = data
        elif movie_number == 'movie_2_data':
            movie_2_read = data
        elif movie_number == 'movie_3_data':
            movie_3_read = data

    # Prints information read from file
    print("Movie 1: " + str(movie_1_read) + "\n\n\n")
    print("Movie 2: " + str(movie_2_read) + "\n\n\n")
    print("Movie 3: " + str(movie_3_read) + "\n\n\n")

#Exception if the file was not found.
except FileNotFoundError:
        print("Error: The file " + pickle_file + " was not found.")     
 