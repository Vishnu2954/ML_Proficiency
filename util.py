import json
import pickle
import os

__que = None
__datacolumns = None
__model = None

def get_que():
    return __que

def load_artifacts():
    global __datacolumns
    global __que
    global __model

    try:
        with open('columns.json', 'r') as f:
            __datacolumns = json.load(f)['datacolumns']
            __que = __datacolumns[0:]
    except Exception as e:
        print(f"Error loading columns.json: {e}")

    try:
        with open('MLprojectRFC', 'rb') as f:
            __model = pickle.load(f)
    except Exception as e:
        print(f"Error loading MLprojectRFC: {e}")

    print(f"Loaded __que: {__que}")

def encode_user_input(response):
    encoding_mapping = {'yes': 1, 'no': 0, 'not sure': 0.5}
    return encoding_mapping.get(response.lower(), 0) if response else 0.5

def predict_user_proficiency(user_responses):
    print("User Responses:", user_responses)

    user_input = [encode_user_input(user_responses.get(col, 'not sure')) for col in get_que()]

    print("User Input:", user_input)

    predicted_level_encoded = __model.predict([user_input])[0]
    proficiency_levels = {0: 'Beginner', 1: 'Intermediate', 2: 'Advanced'}
    predicted_level = proficiency_levels.get(predicted_level_encoded, 'Unknown')

    print("Predicted Level Encoded:", predicted_level_encoded)
    print("Predicted Level:", predicted_level)

    return predicted_level

if __name__ == "__main__":
    load_artifacts()
    print(get_que())
