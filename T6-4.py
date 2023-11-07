# We have a number
number = int(input("Enter string : "))
# converting to string
number = str(number)
# Storing first and last digit in a variable
first_digit = int(number[0]) # converting  first and last string with indexing  to integer
last_digit = int(number[-1])
# Adding these two variables
addition = first_digit + last_digit #8 +5
print("Sum of first and last digit for a given value:",addition)