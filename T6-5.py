def minimize_mango_difference(mangoes, m):
    mangoes.sort()
    left, right = 0, len(mangoes) - 1
    min_difference = float('inf')
    while left <= right:
        current_difference = mangoes[right] - mangoes[left]
        min_difference = min(min_difference, current_difference)
        if m > 2:
            left += 1
            right -= 1
        elif m == 2:
            left += 1
    return min_difference
n = [19,15,16,18,10,2,100,155]
m = 3
min_difference = minimize_mango_difference(n, m)
print("Minimum difference:", min_difference)
