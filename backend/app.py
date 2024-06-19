from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('model/sardine_predictor_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    temperature = data['temperature']
    salinity = data['salinity']
    prediction = model.predict([[temperature, salinity]])[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
