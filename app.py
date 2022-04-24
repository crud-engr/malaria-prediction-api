from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
import numpy as np
import pickle
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
        print('DATA:::::', data)
        model = joblib.load(open('mal_ty_joblib', 'rb'))
        prob_res = model.predict_proba([np.array(list(data.values()))])
        prediction = model.predict([np.array(list(data.values()))])[0]

        accuracy = 0

        if prediction == 0:
            prediction = 'Non-malaria Infection'
            accuracy = round(prob_res[0][0] * 100)
        elif prediction == 1:
            prediction = 'Severe Malaria'
            accuracy = round(prob_res[0][1] * 100)
        else:
            prediction = 'Uncomplicated Malaria'
            accuracy = round(prob_res[0][2] * 100)

        print('PREDICTION:::::', prediction)
        print('ACCURACY:::::', accuracy)
        print('PREDICTION:::::', prediction)

        return {
            "analysis": {
                "predict_type": prediction,
                "accuracy_level": accuracy,
            },
        }, 200

    except ValueError as e:
        return {e.args[0]}, 400

if __name__ == "__main__":
    app.run(debug=True)