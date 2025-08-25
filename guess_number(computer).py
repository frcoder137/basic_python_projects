import random

def guess_the_number():
    low = int(input("Enter minimum >> "))
    high = int(input("Enter maximum >> "))
    print(f'Consider a number between {low} and {high}')
    attempts = 0

    while True:
        guess = random.randint(low, high)
        attempts += 1

        answer = input(f'Computer guessed {guess} is it correct, low or high (c / l / h)?  ').lower()

        if answer == 'c':
            break
        elif answer == 'l':
            low = guess + 1
        elif answer == 'h':
            high = guess - 1

    return attempts, answer

attempts, number = guess_the_number()
print(f'Computer guessed the answer "{number}" in {attempts} attempts!')

