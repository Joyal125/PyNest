# Program to find the sum of digits of a number

num = int(input("Enter a number: "))
sum_of_digits = 0

while num > 0:
    digit = num % 10       # get the last digit
    sum_of_digits += digit # add it to the sum
    num //= 10             # remove the last digit

print("Sum of digits:", sum_of_digits)
