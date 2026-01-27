import random
import os

secret_number = int(random.randrange(0, 100))
print(secret_number)

def choose_option():
    try:
        user_option = int(input("Guess the number: \n"))
        if user_option == secret_number:
            print("You guessed the secret number!")
        elif user_option < secret_number:
            print("\nThe secret number is higher than the guess.\n")
            choose_option()
        else:
            print("\nThe seret number is less than the guess.\n")
            choose_option()
    except:
        return "ERROR: Invalid guess."

def main():
    os.system("cls")
    choose_option()

if __name__ == "__main__":
    main()