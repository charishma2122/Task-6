a = [10,501,22,37,100,999,87,351]
b = []
# print((len(a)))
def is_happy(a):
    for i in range (len(a)):
        x = a[i] # while iterating the loop each value is assigned to x variable
        while x!=1 and x!=4: #  checking whether value is not equal to 1 and 4
            tempsum = 0 # initializing tempsum as zero
            for digit in str(x):
                tempsum += int(digit) ** 2 # squares each number in list
            x = tempsum
        if x == 1: # checking whether final value not equal to 1
            b.append(a[i]) #adding the index to b variable
    return b
print("Happy numbers: ",is_happy(a)) # calling the function with the list of inputs and generating the output