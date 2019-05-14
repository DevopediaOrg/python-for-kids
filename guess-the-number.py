import random

selected_number = random.randint(1, 50)

print("I've selected a number between 1 and 50. Can you guess the number?")

attempt = 0
while True:
    attempt += 1
    guess = input("Your guess: ")
    try:
        guess = int(guess)
    except ValueError:
        print("Your guess is not an integer. Guess again.")
    
    if guess < selected_number:
        print("Your guess is lower than the correct number. Try again.")
    elif guess > selected_number:
        print("Your guess is higher than the correct number. Try again.")
    else:
        print("Congrats! You've guessed the correct number. It's", selected_number)
        print("You took", attempt, "attempts to guess correctly.")
        exit(0)