"""
Instructions:
Given a string, remove any repeated letters.

"""

def removeRepeats(given_str):
    check_array = []
    new_str = []
	
    for i in range(0,len(given_str)):
        if i == 0:
            check_array+= given_str[0]
        else:
            if given_str[i] not in check_array:
                check_array += given_str[i]	
    new_str.append("".join(check_array))
    return new_str
	


if __name__ == "__main__":
    given_str = "safgrwoboenboenviiavneirbn"
    trimmed_str = removeRepeats(given_str)
    
    print(" Your old bulky string was: {} \n Your new sleek and trimmed string is: {}".format(given_str, trimmed_str[0])) 
