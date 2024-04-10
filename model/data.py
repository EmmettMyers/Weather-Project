import requests
from cities import *
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# returns a dictionary with current weather forecast data for the largest 100 U.S. cities
# keys: city, values: array of weather variables 
# weather variables: (temperature, humidity, dew point, precipitation, wind speed, wind direction)
# DO NOT RUN THIS TOO MUCH, ONLY CAN RUN 99 TIMES PER DAY UNTIL URL EXPIRES FOR THAT DAY
def get_model_training_data():
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # stores all current weather for each city
    cities_current_weather = {}

    for city, coordinates in cities_coordinates.items():
        latitude = coordinates[0]
        longitude = coordinates[1]

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "precipitation", "wind_speed_10m", "wind_direction_10m"]
        }
        responses = openmeteo.weather_api(url, params=params)
        data = responses[0]

        hourly = data.Hourly()
        hourly_temperature_2m = (hourly.Variables(0).ValuesAsNumpy()[0] * 9/5) + 32
        hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()[0]
        hourly_dew_point_2m = (hourly.Variables(2).ValuesAsNumpy()[0] * 9/5) + 32
        hourly_precipitation = hourly.Variables(3).ValuesAsNumpy()[0]
        hourly_wind_speed_10m = hourly.Variables(4).ValuesAsNumpy()[0]
        hourly_wind_direction_10m = hourly.Variables(5).ValuesAsNumpy()[0]

        cities_current_weather[city] = {
            "Temperature": hourly_temperature_2m,
            "Humidity": hourly_relative_humidity_2m,
            "Dew Point": hourly_dew_point_2m,
            "Precipitation": hourly_precipitation,
            "Wind Speed": hourly_wind_speed_10m,
            "Wind Direction": hourly_wind_direction_10m
        }

    print(cities_current_weather)
    print(cities_current_weather['Los Angeles, California'])
    return cities_current_weather
