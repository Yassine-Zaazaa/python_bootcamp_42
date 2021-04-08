import sys

def reverse_string(string):
    string  = string[::-1]
    new_string = ""
    for i in string:
        if i.isupper():
            new_string += i.lower()
        else:
            new_string += i.upper()
    return new_string


if __name__=='__main__' :
    string = ""
    for i in range(1, len(sys.argv)):
        string += " " + sys.argv[i]
    print(reverse_string(string))
        
        
