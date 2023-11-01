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
    # Record headband data

    # Store values for each movie
    # ** Currently stroes filler data until SDK can be implemented
    # ** Will add flags 
    recorded_user_data['movie_1_data'] = ['1111', '11', '1']
    recorded_user_data['movie_2_data'] = ['2222', '2', '2']
    recorded_user_data['movie_3_data'] = ['3333', '3', '3']
    recorded_user_data['movie_4_data'] = ['4444', '4', '4']
    recorded_user_data['movie_5_data'] = ['5555', '55', '5']
    return ["Finished Recording"]

'''
hb_record = Flask(__name__)

# Dictionary to store recording status for each video
recording_status = {
    "video1": False,
    "video2": False,
    "video3": False,
    "video4": False,
    "video5": False,
}

@hb_record.route('/index', methods=['POST'])
def control_recording():
    data = request.get_json()
    action = data.get('action')
    video_id = data.get('videoId')

    if action == 'startRecording':
        if not recording_status[video_id]:
            # Start recording logic for the specified video
            recording_status[video_id] = True
            return jsonify({"message": f"Recording started for {video_id}"})
        else:
            return jsonify({"message": f"Recording already started for {video_id}"})

    elif action == 'stopRecording':
        if recording_status[video_id]:
            # Stop recording logic for the specified video
            recording_status[video_id] = False
            return jsonify({"message": f"Recording stopped for {video_id}"})
        else:
            return jsonify({"message": f"Recording not started for {video_id}"})
'''