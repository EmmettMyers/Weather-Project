from flask import Flask, request, jsonify
from flask_cors import CORS
import MachineLearningModel 

app = Flask(__name__)
CORS(app)  

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = MachineLearningModel.predict_city(
        temperature=data['temperature'], 
        humidity=data['humidity'], 
        dew_point=data['dewPoint'], 
        precipitation=data['precipitation'], 
        wind_speed=data['windSpeed'], 
        wind_direction=data['windDirection']
    )
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
