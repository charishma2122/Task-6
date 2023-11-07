def first_non_repeating_element(lst):
    value_count = {}  # Dictionary to store the count of each value

    # Count the occurrences of each value in the list
    for value in lst:
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1

    # Find the first non-repeating value
    for value in lst:
        if value_count[value] == 1:
            return value
# Example usage:
my_list =  [2,1,2,3,2,4,5]
result = first_non_repeating_element(my_list)
if result is not None:
    print("First non-repeating element:", result) #1
else:
    print("No non-repeating elements found in the list.")

