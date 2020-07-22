'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):

    number_array1 = []
    number_array2 = []

    for number in arr:
        if number not in number_array1:
            number_array1.append(number)
        else:
            number_array2.append(number)
    
    for number in number_array1:
        if number not in number_array2:
            return number
    
    return -1






if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")