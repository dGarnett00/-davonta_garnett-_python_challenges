def find_max(lst):
    if not lst:
        raise ValueError("The list is empty.")
    max_value = lst[0]
    max_index = 0
    index = 1
    while index < len(lst):
        if lst[index] > max_value:
            max_value = lst[index]
            max_index = index
        index += 1
    return max_value, max_index