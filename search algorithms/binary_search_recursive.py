''' 
    Program in python to implement Binary Search
    Binary Search works only on sorted array
    The approach to write the program here is Recursive
    Time Complexity : O(log n)
'''

def binary_search_recursive(input_Array, key_to_search, left, right):
    if left > right:
        return "Not Found"
    else:
        middle = (left + right)//2
        if key_to_search == input_Array[middle]:
            return middle
        elif key_to_search < input_Array[middle]:
            return binary_search_recursive(input_Array, key_to_search, left, middle -1)
        elif key_to_search > input_Array[middle]:
            return binary_search_recursive(input_Array, key_to_search, middle + 1, right)
        
if __name__ == "__main__":
    input_array = [99,12,44,32,67,16,80]
    found_at = binary_search_recursive(sorted(input_array), 80, 0, len(input_array))      #The sorted function here uses TIM SORT
    print("Found at index:", found_at)