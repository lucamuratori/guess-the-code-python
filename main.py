import random

NUM_DIGITS = 3
MAX_GUESSES = 10

print(f"I am thinking of a {NUM_DIGITS} number, with no repeated digits."
      f"\nTry to guess what it is. Here are some clues: "
      f"\nWhen I say:    That means:"
      f"\n  Pico         One digit is correct but in the wrong position."
      f"\n  Fermi        One digit is correct and in the right position."
      f"\n  Bagels       No digit is correct."
      f"\nFor example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico."
      f"\nYou have {MAX_GUESSES} guesses.")

def get_number():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def check_code(guess, secret_code):
    clues = []
    if guess == secret_code:
        return "Congratulations, this is the correct code!"
    elif guess != secret_code:
        for i in range(len(guess)):
            if guess[i] == secret_code[i]:
                clues.append("Fermi")
            elif guess[i] in secret_code:
                clues.append("Pico")
        if not clues:
            clues.append("bagels")
        clues.sort()
        return print(' '.join(clues))


while True:
    guess_counter = 1
    secret_code = get_number()
    while guess_counter <= MAX_GUESSES:
        guess = ''
        while len(guess) != len(secret_code):
            guess = str(input(f"Your guessed {NUM_DIGITS} digit code is: "))
        check_code(guess, secret_code)

        if guess == secret_code:
            break
        guess_counter += 1
        if guess_counter > MAX_GUESSES:
            print("You ran out of guesses.")
        else:
            print(f"you have {MAX_GUESSES - guess_counter + 1} guesses left.")
    print("Do you want to play again? (y/n)")
    if not input("/> ").lower().startswith('y'):
        break


