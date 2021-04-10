from random import randint


print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print("\n\n")

secret_number = randint(1,99)
counter = 1
var = True
while var == True:
    print("What's your guess between 1 and 99?")
    guess = input(">> ")
    if guess.isdigit():
        guess = int(guess)
        if guess > secret_number:
            print("Too high !")
        elif guess < secret_number:
            print("Too low!")
        elif guess == secret_number:
            if counter > 1:
                print("Congratulations, you've got it!")
                print(f"You won in {counter} attempts!")
            elif counter == 1:
                if secret_number == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                print("Congratulations! You got it on your first try!")
            var = False
    elif guess.lower() == "exit":
        print("Goodbye!")
        var = False
    else:
        print("That's not a number.")
    counter += 1