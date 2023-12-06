from flask import g                         
from tools.logging import logger   
from neurosdk.cmn_types import * 
import copy
from auth import request_username
import time

# Custom data type to store username and brainwave data
user_data = {
    # Store current username 
    'cur_username': "",
    # Store brainwave data for the movies
    'movie_data': [], 
}

# Creates user_data template
recorded_user_data = copy.deepcopy(user_data)

# Stores the value for movies status
movie_finished = False

# Update the value of current movie to passed value
def update_movie_status(data):
    global movie_finished
    movie_finished = data

# Appends data to user data structure
def update_user_data(data):
    global recorded_user_data

    # Appends brain wave data to array
    recorded_user_data['movie_data'].append(data)

# Stores all the recorded user data from the movies
def handle_request():
    # Get username from current session, store it in the object
    recorded_user_data['cur_username'] = request_username()
    
    # Stores filler data if headband not connected.
    if g.hb == None:

        update_user_data([BrainBitSignalData(PackNum=16, Marker=0, O1=0.07790878096464249, O2=0.05911756431347305, T3=0.11504527573134969, T4=0.1162186777292993), BrainBitSignalData(PackNum=16, Marker=0, O1=0.07777869966382948, O2=0.059174784827027156, T3=0.11500674725222326, T4=0.11590892401592638), BrainBitSignalData(PackNum=17, Marker=0, O1=0.07771423121855853, O2=0.0592472641441957, T3=0.11495219702930168, T4=0.11572467396228214), BrainBitSignalData(PackNum=17, Marker=0, O1=0.07770355005602843, O2=0.05918317716901509, T3=0.11492358677252462, T4=0.11577159478339652)])
        update_user_data([BrainBitSignalData(PackNum=52, Marker=0, O1=0.0764740719547958, O2=0.058433969911546625, T3=0.11210719309539137, T4=0.11390468016117111), BrainBitSignalData(PackNum=52, Marker=0, O1=0.07642333643277782, O2=0.05840650406504065, T3=0.11206599432563241, T4=0.11372348186824977), BrainBitSignalData(PackNum=53, Marker=0, O1=0.07646300932217534, O2=0.05846258016832368, T3=0.11204310612021076, T4=0.11382380850201464), BrainBitSignalData(PackNum=53, Marker=0, O1=0.07653358128889207, O2=0.0584759316214863, T3=0.11205416875283122, T4=0.11396762272608063)])
        update_user_data([BrainBitSignalData(PackNum=54, Marker=0, O1=0.0764088405693441, O2=0.058449228715161054, T3=0.11200801087189757, T4=0.11356021266957537), BrainBitSignalData(PackNum=54, Marker=0, O1=0.07644660610828982, O2=0.05843587726199843, T3=0.11197024533295187, T4=0.11359759673843073), BrainBitSignalData(PackNum=55, Marker=0, O1=0.07646377226235605, O2=0.058439310492811675, T3=0.11193133538373508, T4=0.11363231051665355), BrainBitSignalData(PackNum=55, Marker=0, O1=0.0765129819040126, O2=0.058399637603414156, T3=0.11191035452876523, T4=0.11376735092864125)])
        update_user_data([BrainBitSignalData(PackNum=56, Marker=0, O1=0.0763729823808502, O2=0.05840917435567318, T3=0.11184741196385571, T4=0.11337825143647332), BrainBitSignalData(PackNum=56, Marker=0, O1=0.07644469875783802, O2=0.05845151753570322, T3=0.11185351548530148, T4=0.11353274682306941), BrainBitSignalData(PackNum=57, Marker=0, O1=0.07644889492883199, O2=0.05844236225353456, T3=0.11183901962186778, T4=0.1136056076103283), BrainBitSignalData(PackNum=57, Marker=0, O1=0.07644355434756694, O2=0.05843816608254059, T3=0.11180621319409675, T4=0.11360713349068975)])

        # Loop while videos are being watched
        while(movie_finished == False):
            # Sleep for time between checking value
            time.sleep(1)
        
        # Data recorded so return
        logger.debug("Finished Test Recording")
        return ["Finished Recording Test"]
    
    # Stores head band data
    else:
        # Iterate, checking for final movie value
        while(movie_finished == False):
            # Sleep for time between choosing videos
            time.sleep(1)

        # Data has been recorded so return
        logger.debug("Finished Recording")
        return ["Finished Recording"]
    
