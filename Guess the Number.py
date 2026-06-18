import random

print("=" * 40)
print("Welcome to the Number Guessing Game!")
print("=" * 40)

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("\nEnter your guess (1-100): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")

        elif guess > secret_number:
            print("Too high! Try a lower number.")

        else:
            print("\nCongratulations!")
            print(f"You guessed the number {secret_number} correctly.")
            print(f"It took you {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")

