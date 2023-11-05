import pickle

# Ask the user what pickle file they want to read.
question = "Pickle file to read:\n"
pickle_file = input(question)
pickle_file = "hb_pickled_user_data/" + pickle_file
# We can read the data from the pickle file and print it.
try:
    with open(pickle_file, 'rb') as file:
        loaded_user_data = pickle.load(file)

    print(loaded_user_data)

#Exception if the file was not found.
except FileNotFoundError:
        print("Error: The file " + pickle_file + " was not found.")     
 