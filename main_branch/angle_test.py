import math
player = (5, 5)
food = (3, 3)
distance_x = food[0] - player[0]
distance_y = food[1] - player[1]
angle = math.atan2(distance_y, distance_x)

print(angle)