from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/mlq')
def mlq():
    return render_template('mlq.html')

@app.route('/get_que', methods=['GET'])
def get_que():
    response = jsonify({
        'question': util.get_que()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_proficiency', methods=['POST'])
def predict_proficiency():
    user_responses = request.json
    print("Received Data:", user_responses)

    predicted_level = util.predict_user_proficiency(user_responses)

    response = jsonify({
        'predicted_level': predicted_level
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Loading artifacts...")
    util.load_artifacts()
    print("Artifacts loaded.")
    app.run(debug=False)



