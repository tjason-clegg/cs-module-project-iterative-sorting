from iterative_sorting import selection_sort


def linear_search(arr, target):
    # Your code here

    # Loop over the list
    for i in range(len(arr)):
        # Check to see if the current index is the same as the target value
        if arr[i] == target:
            return i

    return -1   # not found

# Compare the item in the middle of the data set to the item we are searching for.
# If it is the same, the we can stop since we found it.
# Else, if the item we are searching for is LESS then the item thats in the middle:
    # We can eliminate the right hand side of the list, then repeat step 1, searching only the left hand side of the list.
# Else, the item we are searching for is GREATER then the item in the middle
    # We can eliminate the left hand side of the list, then repeat step 1, searching onlt the right hand side of the list.

# Write an iterative implementation of Binary Search


def binary_search(arr, target, start=0, end=None):
    arr = selection_sort(arr)

    # Determine the end point
    if end is None:
        end = len(arr) - 1

    # If the starting point is greater then the end point, return not found
    if start > end:
        return - 1

    # // Divides and returns the intger value of the quotient, then dumps the remainder

    # Determine the middle of the list
    mid = (start + end) // 2

    # If the middle of the list is the same as the target, return the target index
    if target == arr[mid]:
        return mid

    # If the target is less then the middle index value, start the process again searching only the left side of the list
    if target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)

    # If the target is greater then the middle index value, start the process again searching only the right side of the list
    return binary_search(arr, target, mid + 1, end)
