# Convert inches to various units

inches = float(input("Enter measurement in inches: "))

# Conversions
feet = inches / 12
yards = inches / 36
centimeters = inches * 2.54
meters = inches / 39.37

# Output
print("Feet:", feet)
print("Yards:", yards)
print("Centimeters:", centimeters)
print("Meters:", meters)
