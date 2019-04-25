"""
Instructions:
Given an array of integers, write a method to sum the elements in the array, 
knowing that some of the elements may be very large integers.


"""

# solving without using sum function
def sumArray(arr): 
    result = 0
    for i in arr:
        result += i
    return str(result)


if __name__ == "__main__": 
# display sum 
    arr = [5254, 2354 , 263265, 34265767] 
    print ("Sum of the array is: {}".format(sumArray(arr)))

