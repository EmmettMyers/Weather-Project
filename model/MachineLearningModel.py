from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import fetchData

#Fetch data from api script
api_data = fetchData.get_model_training_data()  
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

df = pd.DataFrame(data, columns=["Temperature", "Humidity", "Dew Point", "Precipitation", "Wind Speed", "Wind Direction"])
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)  

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy:.2%}")

# Example new data -- Should be closest to LA, CA
new_data = pd.DataFrame(np.array([[75, 25, 37, 0, 16, 256]]),
                        columns=["Temperature", "Humidity", "Dew Point", "Precipitation", "Wind Speed", "Wind Direction"])

predicted_label = model.predict(new_data)

predicted_city = label_encoder.inverse_transform(predicted_label)
print(f"Predicted city: {predicted_city[0]}")
