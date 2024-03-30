def find_min_max(arr):
    if len(arr) == 0:
        return None, None
    else:
        return min(arr), max(arr)
numbers = [5, 8, 1, 10, 3]
minimum, maximum = find_min_max(numbers)
print("Minimum value:", minimum)
print("Maximum value:", maximum)
