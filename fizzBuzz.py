""" 
FizzBuzz
You guessed it, the classic FizzBuzz challenge

Write a program that prints the numbers from 1 to 100. 
However, For multiples of three print “Fizz” instead of the number
For the multiples of five print “Buzz”. 

For numbers which are multiples of both three and five print “FizzBuzz”.
"""
def fizzBuzz ():
    for i in range(1, 101):
        if i % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


if __name__ == "__main__":
    fizzBuzz()