''' 
    Program in python to implement Linear Search:
    Time Complexity : O(n)
'''
def linear_search(Input_Array, key_to_search):
    index = 0
    while index < len(Input_Array):
        if Input_Array[index] == key_to_search:
            return index
        index = index + 1
    return -1

if __name__ == "__main__":
    input_array = [99,12,44,32,67,16,80]
    found_at = linear_search(input_array, 32)
    print("Found at index:", found_at)