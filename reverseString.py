"""
Instructions:
Given a string, reverse it.

"""

def reverseStr(initial_str): 
    reversed_str = ""
    for i in initial_str:
        reversed_str = i + reversed_str
    return reversed_str 

if __name__ == "__main__":
    initial_string = "Reverse me"
    print ("The original string is : {}".format(initial_string)) 
    print ("The reversed string is : {}".format(reverseStr(initial_string)))