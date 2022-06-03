'''
    Selection Sort Algorithm in python
    Time Complexity: O(n ^ 2)
'''

def selection_sort(input_array):
    for i in range(0, len(input_array)-1):
        position = i
        for j in range(i+1, len(input_array)):
            if input_array[j] < input_array[position]:
                position = j
        #Swaping the elements
        input_array[i], input_array[position] = input_array[position], input_array[i]
        
    return input_array       # Returning the Sorted Array

if __name__ == "__main__":
    unsorted_array = [99,12,44,32,67,16,80]
    print("Unsorted Array is:", unsorted_array)
    sorted_array = selection_sort(unsorted_array)
    print("Sorted Array is:", sorted_array)