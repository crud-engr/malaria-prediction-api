from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
import numpy as np
import joblib

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def get():
    return {"data": "Welcome to malaria and typhoid prediction api!"}

@app.route('/api/analyse', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        model = joblib.load(open('mal_ty_joblib', 'rb'))
        prediction = model.predict([np.array(list(data.values()))])[0]

        if prediction == 0:
            prediction = 'Non-malaria Infection'
        elif prediction == 1:
            prediction = 'Severe Malaria'
        else:
            prediction = 'Uncomplicated Malaria'

        return {
            "analysis": {
                "predict_type": prediction,
            },
        }, 200

    except ValueError as e:
        return {e}, 400

if __name__ == "__main__":
    app.run(debug=True)