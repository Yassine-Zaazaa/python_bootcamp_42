import sys

def even_odd_zero(number):
    if number % 2 == 0:
        print("I'm Even.")
    elif number == 0:
        print("I'm Zero.")
    else:
        print("I'm Odd.")
  
    
if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("ERROR")
    else:
        even_odd_zero(int(sys.argv[1]))     