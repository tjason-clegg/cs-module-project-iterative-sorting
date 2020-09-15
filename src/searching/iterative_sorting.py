# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # Loop over the list, using the current index and length of the list
        for s in range(cur_index, len(arr)):
            # if the current index is smaller then the previous smallest_index, then make the current index the new smallest_index
            if arr[s] < arr[smallest_index]:
                smallest_index = s

        # TO-DO: swap
        # Your code here

        # Swap the current index(cur_index) amd the smallest index(smallest_index)
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

        # Add 1 and set current index to the new index
        cur_index += 1

        # Set the smallest index to the current index
        smallest_index = cur_index

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    # loop over the elements in the list and and remove 1
    for i in range(len(arr) - 1):
        # Loop over the list and subtract the length by the current index and 1
        for x in range(0, len(arr) - i - 1):
            # If the list at the index is greater the the index plus 1, then set list and list index plus 1 to the list plus 1 and the list's index
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
