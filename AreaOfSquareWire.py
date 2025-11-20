import math

# Given values
angle = 60
radius = 42

# Step 1: Calculate arc length
arc_length = (angle / 360) * 2 * math.pi * radius

# Step 2: Arc converts to square perimeter
side = arc_length / 4

# Step 3: Area of square
area = side * side

print("Arc Length:", arc_length)
print("Side of Square:", side)
print("Area of Square:", area)
