numbers = [10,501,22,37,100,999,87,351]
x = []
y = []
for num in numbers:   #   iterate with the value when you don't need the index
    for m in range(2, (num // 2) + 1):
        if num % m == 0:
            # print('This is not prime', num)
            x.append(num)
            non_prime = list(x)
            break
    else:
        y.append(num)   #   use `append` to insert at the tail of the list
        prime = list(y)
print('This is prime: ', prime)
print('This is not prime: ', non_prime)
# print(x, y)
# print(x)