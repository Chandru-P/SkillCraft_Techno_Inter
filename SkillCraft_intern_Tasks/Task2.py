import random
def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I have generated a random number between 1 and 100.")

    random_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
            break
guess_the_number()
