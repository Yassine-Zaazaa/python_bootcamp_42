import sys

def reverse_string(string):
    string  = string[::-1]
    reversed_string = ""
    for i in string:
        if i.isupper():
            reversed_string += i.lower()
        else:
            reversed_string += i.upper()
    return reversed_string


if __name__=='__main__' :
    string = ""
    for i in range(1, len(sys.argv)):
        string += " " + sys.argv[i]
    print(reverse_string(string))
        
        