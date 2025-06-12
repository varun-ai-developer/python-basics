import random

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 to 10: "))
    attempts += 1

    if guess == secret_number:
        print("🎉 Correct! You guessed it in", attempts, "attempts.")
        break
    elif guess < secret_number:
        print("📉 Too low! Try again.")
    else:
        print("📈 Too high! Try again.")