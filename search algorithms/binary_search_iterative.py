''' 
    Program in python to implement Binary Search
    Binary Search works only on sorted array
    The approach to write the program here is Iterative
    Time Complexity: O(log n)
'''

def binary_search(input_Array, key_to_search):
    left = 0
    right = len(input_Array) - 1
    while left < right:
        middle = (left + right)//2
        if key_to_search == input_Array[middle]:
            return middle
        elif key_to_search < input_Array[middle]:
            right = middle - 1
        elif key_to_search > input_Array[middle] :
            left = middle + 1
    return "Not Found"

if __name__ == "__main__":
    input_array = [99,12,44,32,67,16,80]
    found_at = binary_search(sorted(input_array), 80)      #The sorted function here uses TIM SORT
    print("Found at index:", found_at)