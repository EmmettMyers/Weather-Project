from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import fetchData  

def predict_city(temperature, humidity, dew_point, precipitation, wind_speed, wind_direction):
    # Fetch data from API
    api_data = fetchData.get_model_training_data()
    
    # Prepare the dataset
    data = []
    labels = []
    for city, weather in api_data.items():
        labels.append(city)
        features = [
            weather["Temperature"],
            weather["Humidity"],
            weather["Dew Point"],
            weather["Precipitation"],
            weather["Wind Speed"],
            weather["Wind Direction"]
        ]
        data.append(features)
    
    # Data preprocessing
    df = pd.DataFrame(data, columns=["Temperature", "Humidity", "Dew Point", "Precipitation", "Wind Speed", "Wind Direction"])
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)
    
    # Splitting the dataset
    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Model evaluation
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model training accuracy: {accuracy:.2%}")
    
    # Prepare new data for prediction
    new_data = pd.DataFrame(np.array([[temperature, humidity, dew_point, precipitation, wind_speed, wind_direction]]),
                            columns=["Temperature", "Humidity", "Dew Point", "Precipitation", "Wind Speed", "Wind Direction"])
    
    # Predict
    predicted_label = model.predict(new_data)
    predicted_city = label_encoder.inverse_transform(predicted_label)

    #Return
    print(f"Predicted city: {predicted_city[0]}")
    return predicted_city[0]
