from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

data = pd.read_csv('./test.csv')
print(data.head())

#Inputs from User
Month = 'January'
Temperature = 90
Wind = 20
Pressure = 10
Humitity = 20
Precipiation = 1 # 1 or 0

#Filter by month
#data = data[data['month'] == 'January']

X = data[['Temperature', 'Wind', 'Pressure', 'Humitity', 'Precipitation']]
y = data['Location']

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

new_data = pd.DataFrame(data=[[10, 60, 25, 90, 0]], columns=['Temperature', 'Wind', 'Pressure', 'Humitity', 'Precipitation'])
predicted_label = model.predict(new_data)

predicted_location = encoder.inverse_transform(predicted_label)

print(f'Predicted Location: {predicted_location[0]}')
