from flask import Flask, request, jsonify
from flask_cors import CORS
import MachineLearningModel
from EuclideanModel import find_most_similar_cities

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    """
    predictions = MachineLearningModel.predict_city(
        temperature=data['temperature'], 
        humidity=data['humidity'], 
        dew_point=data['dewPoint'], 
        precipitation=data['precipitation'], 
        wind_speed=data['windSpeed'], 
        wind_direction=data['windDirection']
    )
    """

    user_values = {
        'Temperature': data['temperature'],
        'Humidity': data['humidity'],
        'Dew Point': data['dewPoint'],
        'Precipitation': data['precipitation'],
        'Wind Speed': data['windSpeed'],
        'Wind Direction': data['windDirection']
    }
    predictions = find_most_similar_cities(user_values)
    return jsonify({'predictions': predictions})

if __name__ == '__main__':
    app.run(debug=True)
