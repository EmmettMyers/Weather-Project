from flask import Flask, request, jsonify
from flask_cors import CORS
from EuclideanModel import find_most_similar_cities

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
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
