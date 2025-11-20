# Arithmetic Progression - nth term and sum of n terms

# Input values
a = float(input("Enter the first term (a): "))
d = float(input("Enter the common difference (d): "))
n = int(input("Enter the term number (n): "))

# nth term
nth_term = a + (n - 1) * d

# sum of first n terms
sum_n = (n / 2) * (2 * a + (n - 1) * d)

# Output results
print("Nth term of the AP:", nth_term)
print("Sum of first n terms:", sum_n)
