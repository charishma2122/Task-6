def find_triplets_with_sum(arr, target_sum):
    triplets = []
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    triplets.append([arr[i], arr[j], arr[k]])
    return triplets
# Example usage:
my_list = [10, 20, 30, 9]
target = 59
result = find_triplets_with_sum(my_list, target)
if result:
    print("Triplets with sum", target, "are:", result)
else:
    print("No triplets found with the given sum.")
