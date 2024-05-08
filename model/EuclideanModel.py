import heapq
import math
import FetchData

def euclidean_distance(user_values, city_values):
    distance = 0
    for param in user_values:
        distance += (float(user_values[param]) - float(city_values[param]))**2
    return math.sqrt(distance)

def calculate_percentage_similarity(user_values, city_values):
    total_difference = sum(abs(float(user_values[param]) - float(city_values[param])) for param in user_values)
    total_possible_difference = len(user_values) * max(max(float(user_values[param]), float(city_values[param])) for param in user_values)
    similarity_percentage = ((total_possible_difference - total_difference) / total_possible_difference) * 100
    return round(similarity_percentage, 2)

def find_most_similar_cities(user_values, k=5):
    api_data = FetchData.get_model_training_data()
    heap = []
    
    for city, city_values in api_data.items():
        distance = euclidean_distance(user_values, city_values)
        similarity_percentage = calculate_percentage_similarity(user_values, city_values)
        heapq.heappush(heap, (distance, city, similarity_percentage))
    
    most_similar_cities = []
    for _ in range(min(k, len(heap))):
        distance, city, similarity_percentage = heapq.heappop(heap)
        most_similar_cities.append((city, similarity_percentage))
    
    return most_similar_cities