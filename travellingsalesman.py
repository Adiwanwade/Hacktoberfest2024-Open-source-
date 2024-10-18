import itertools

def calculate_distance(city1, city2):
    # You can replace this with your actual distance calculation
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def total_distance(route, distances):
    return sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))

def travelling_salesman(cities):
    # Precompute the distance between each pair of cities
    distances = {}
    for (i, city1), (j, city2) in itertools.combinations(enumerate(cities), 2):
        distances[i] = distances.get(i, {})
        distances[j] = distances.get(j, {})
        dist = calculate_distance(city1, city2)
        distances[i][j] = dist
        distances[j][i] = dist

    # Generate all possible routes
    min_distance = float('inf')
    best_route = None

    for perm in itertools.permutations(range(len(cities))):
        # Calculate the distance for the current permutation
        current_distance = total_distance(perm + (perm[0],), distances)  # Returning to start
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = perm

    return best_route, min_distance

# Example usage
cities = [(0, 0), (1, 2), (2, 1), (3, 3)]
best_route, min_distance = travelling_salesman(cities)
print("Best route:", best_route)
print("Minimum distance:", min_distance)
