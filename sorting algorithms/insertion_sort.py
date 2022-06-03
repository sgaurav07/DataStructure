'''
    Insertion Sort Algorithm in python
    The relative ordering of same elements in the array are 
    preserved hence the insertion sort is an stable algorithm
    
    Time Complexity: O(n ^ 2) ------> Worst Case
'''

def insertion_sort(input_array):
    for i in range(1, len(input_array)):
        compare_value = input_array[i]
        position = i
        while position > 0 and input_array[position -1] > compare_value:
            input_array[position] = input_array[position -1]
            position = position - 1
        input_array[position] = compare_value

    return input_array


if __name__ == "__main__":
    unsorted_array = [99,12,44,32,67,16,80]
    print("Unsorted Array is:", unsorted_array)
    sorted_array = insertion_sort(unsorted_array)
    print("Sorted Array is:", sorted_array)