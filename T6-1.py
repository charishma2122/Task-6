
numbers = [10,501,22,37,100,999,87,351]
def split_list_even_odd(numbers): #  defining the function to get the even and odd numbers
    odd_numbers = [number for number in numbers if number % 2 == 1] # Checking the each index in the list whether the remaininder is 1 and asigning to odd number list
    even_numbers = [number for number in numbers if number % 2 == 0] # Checking the each index in the list whether the remaininder is 0 and asigning to even number list
    return odd_numbers, even_numbers
result = split_list_even_odd(numbers) # calling the function and storing the result in a variable
print("Odd numbers in a given list",result[0]) # printing the first index as odd numbers
print("Even numbers in a given list",result[1]) # printing the secong index as even numbers