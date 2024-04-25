# Calculate euclidean distance of each point from (0, 0)

import math

def euclidean_distance(x, y):
    return math.sqrt(x ** 2 + y ** 2)

coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

for index, (x, y) in enumerate(coordinates):
    distance = euclidean_distance(x, y)
    print(f'Distance of the point at index {index} from the origin: {distance:.2f}')