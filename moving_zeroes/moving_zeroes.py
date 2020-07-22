'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    index = 0
    new_array = []
    while index < len(arr):
        number = arr[index]
        if number == 0:
            new_array.insert(len(arr), number)
        else:
            new_array.insert(0, number)
        index += 1
    return new_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")