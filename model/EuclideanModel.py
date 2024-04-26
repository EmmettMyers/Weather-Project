import heapq
import math
import fetchData

def euclidean_distance(user_values, city_values):
    distance = 0
    for param in user_values:
        distance += (float(user_values[param]) - float(city_values[param]))**2
    return math.sqrt(distance)

def find_most_similar_cities(user_values, k=5):
    api_data = fetchData.get_model_training_data()
    heap = []
    
    for city, city_values in api_data.items():
        distance = euclidean_distance(user_values, city_values)
        heapq.heappush(heap, (distance, city))
    
    most_similar_cities = []
    for _ in range(min(k, len(heap))):
        most_similar_cities.append(heapq.heappop(heap)[1])
    
    return most_similar_cities