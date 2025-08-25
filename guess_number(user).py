import random

def guess_the_number():
    low = 1
    high = 100
    number = random.randint(low, high)
    attempts = 0

    while True:
        guess = int(input(f"Guess a number between {low} and {high}:  "))
        attempts += 1

        if guess == number:
            break
        elif guess < number:
            print("Too low!")
            low = guess + 1
        elif guess > number:
            print("Too high!")
            high = guess - 1

    return attempts, guess

attempts, number = guess_the_number()
print(f'Congratulations! You found th answer "{number}" in {attempts} attempts.')
