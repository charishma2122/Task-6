def find_duplicates(*lists):
    # Create an empty dictionary to store value and their counts
    element_counts = {}
    # Iterate through each list
    for lst in lists:
        # Iterate through the value in the current list
        for value in lst:
            # If the value is already in the dictionary, increment its count
            if value in element_counts:
                element_counts[value] += 1
            else:
                element_counts[value] = 1
    # Find value with counts greater than 1 (duplicates)
    duplicates = [value for value, count in element_counts.items() if count > 1]
    return duplicates
# Example usage:
list1 = [1, 3, 4, 5,10]
list2 = [4, 6, 7,10,12,15]
list3 = [7, 8, 9, 9,17,18,15]
duplicates = find_duplicates(list1, list2, list3)

print("Duplicates:", duplicates)
