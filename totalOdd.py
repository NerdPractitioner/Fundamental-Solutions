""" 
Instructions:
Given an array of integers, write a method to total the odd numbers.

"""

# solving without using sum function
def totalOdd(arr): 
    result = 0
    for i in arr:
        if i % 2 > 0:
            result += i
    return str(result)


if __name__ == "__main__": 
# display sum 
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    print ("Sum of the array is: {}".format(totalOdd(arr)))