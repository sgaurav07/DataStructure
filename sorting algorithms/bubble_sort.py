''' 
    Python program to implement bubble sort
    Time complexity of bubble sort is O(n^2) 
'''
def bubbleSort(input_array):
    n = len(input_array)
    for i in range(n):
        for j in range(0, n-i-1):
            if input_array[j] > input_array[j+1] :
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
    return input_array

# Driver code to test above
if __name__ == '__main__':
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted Array is:", unsorted_array)
    sorted_array = bubbleSort(unsorted_array)
    print("Sorted Array is:", sorted_array)