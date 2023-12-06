import pickle
from tools.logging import logger   
from open_calls.hb_record import recorded_user_data

def handle_request():
    # We then pickle the data in a file created for that indiviual user
    pickle_file_name = "./hb_pickled_user_data/" + recorded_user_data['cur_username'] + '_user_data.pickle'
    with open(pickle_file_name, 'wb') as file:
        pickle.dump(recorded_user_data, file)
    logger.debug("File has been pickled")
    return ["File pickled"]
