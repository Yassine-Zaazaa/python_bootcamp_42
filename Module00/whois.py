import sys

def even_odd_zero(number):
    if number.isdigit():
        number = int(number)
        if number == 0:
            return "I'm Zero."
        elif number % 2 == 0:
            return "I'm Even."
        else:
            return "I'm Odd."
    return "ERROR"
    
if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) == 1 :
        print("ERROR")
    else:
        print(even_odd_zero(sys.argv[1]))     