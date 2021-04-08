import sys

def operations(num1, num2):
    print("\n")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        if num2 == 0:
            print("Sum:\t" + str(num1 + num2))
            print("Difference:\t" + str(num1 - num2))
            print("Product:\t" + str(num1 * num2))
            print("Quotient:\tERROR (div by zero)" )
            print("Remainder:\tERROR (modulo by zero)")
        else:
            print("Sum:\t" + str(num1 + num2))
            print("Difference:\t" + str(num1 - num2))
            print("Product:\t" + str(num1 * num2))
            print("Quotient:\t" + str(num1 / num2))
            print("Remainder:\t" + str(num1 % num2))
    else:
        print("InputError: only numbers\n")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n\tpython operations.py 10 3")
        

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("\nInputError: Too many arguments\n")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n\tpython operations.py 10 3")
    elif len(sys.argv) == 1 or len(sys.argv) == 2:
        print("\nUsage: python operations.py <number1> <number2>")
        print("Example:\n\tpython operations.py 10 3")
    else:
        operations(sys.argv[1], sys.argv[2])
        