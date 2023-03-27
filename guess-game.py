# Guessing game
#
secret_number = 9
user_guesses = 0
user_limit = 3

while user_guesses < user_limit:
    user_input = int(input("Oya, guess the number "))
    user_guesses = user_guesses + 1
    if user_input == secret_number:
        print("You gerrit")
        break
else:
    print("Out of luck")
