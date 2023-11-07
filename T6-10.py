def find_sublist_with_sum_zero(lst):
    pre_sum = 0
    pre_sum_dict = {}
    sublist = []
    for index, num in enumerate(lst):
        pre_sum += num

        # If the current prefix sum is 0, return the sublist from the starting
        if pre_sum == 0:
            return lst[:index + 1]

        # If the current prefix sum has been seen before, return the sublist from the previous occurance
        if pre_sum in pre_sum_dict:
            start_index = pre_sum_dict[pre_sum] + 1
            return lst[start_index:index + 1]

        pre_sum_dict[pre_sum] = index

my_list = [4, 2, -3, 1, 6]
result = find_sublist_with_sum_zero(my_list)
if result:
    print("Sublist with sum 0:", result)
else:
    print("No sublist with sum 0 found.",result)
