# Function to generate Pascal's Triangle
def pascal_triangle(n):
    triangle = []  # will store all rows

    for i in range(n):
        row = [1] * (i + 1)   # every row begins and ends with 1
        
        # Fill the middle elements
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle


# Main Program
n = int(input("Enter number of rows: "))

triangle = pascal_triangle(n)

# Print the triangle
for row in triangle:
    print(*row)
