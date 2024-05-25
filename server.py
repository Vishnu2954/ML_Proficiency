from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import util

app = Flask(__name__, template_folder='.')
CORS(app, resources={r"/predict_proficiency": {"origins": "https://ml-proficiency.onrender.com"}})

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/cruise')
def profile():
    return render_template('cruise.html')

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
    util.load_artifacts()
    app.run(debug=False, host='0.0.0.0', port=5000)



