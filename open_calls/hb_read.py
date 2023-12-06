import pickle

# Ask the user what pickle file they want to read.
question = "Pickle file to read:\n"
pickle_file = input(question)
pickle_file = "hb_pickled_user_data/" + pickle_file + "_user_data.pickle"

# We can read the data from the pickle file and print it.
try:
    with open(pickle_file, 'rb') as file:
        loaded_user_data = pickle.load(file)

    # Collects movie data from loaded variable
    for movie_number, data in loaded_user_data.items():
        if movie_number == 'movie_data':
          movie_read = data

    # Prints information read from file
    print("Movie Data: " + str(movie_read))

#Exception if the file was not found.
except FileNotFoundError:
        print("Error: The file " + pickle_file + " was not found.")     
 