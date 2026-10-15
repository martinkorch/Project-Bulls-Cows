import random

DIGITS = 4


def print_intro() -> None:
    """Print the introductory text."""
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")


def generate_secret_number() -> str:
    """Generate a four-digit number with unique digits."""
    digits = list("0123456789")
    first_digit = random.choice(digits[1:])
    digits.remove(first_digit)

    remaining_digits = random.sample(digits, DIGITS - 1)
    return first_digit + "".join(remaining_digits)


def validate_guess(guess: str) -> tuple[bool, str]:
    """Validate the user's guess and return its status and error message."""
    if len(guess) != DIGITS:
        return False, f"Your guess must contain exactly {DIGITS} digits."

    if not guess.isascii() or not guess.isdigit():
        return False, "Your guess must contain only digits (0-9)."

    if guess[0] == "0":
        return False, "Your guess must not start with zero."

    if len(set(guess)) != DIGITS:
        return False, "Your guess must not contain repeated digits."

    return True, ""


def count_bulls_cows(
    secret: str, guess: str
) -> tuple[int, int]:
    """Count bulls and cows and return both values."""
    bulls = sum(
        secret_digit == guess_digit
        for secret_digit, guess_digit in zip(secret, guess)
    )

    cows = sum(
        min(secret.count(digit), guess.count(digit))
        for digit in set(guess)
    ) - bulls

    return bulls, cows


def pluralize(word: str, count: int) -> str:
    """Return the singular or plural form of a word."""
    return word if count == 1 else f"{word}s"


def format_result(bulls: int, cows: int) -> str:
    """Format the result with correct singular and plural forms."""
    bull_word = pluralize("bull", bulls)
    cow_word = pluralize("cow", cows)

    return f"{bulls} {bull_word}, {cows} {cow_word}"


def game_loop(secret: str) -> None:
    """Run the game until the player guesses the secret number."""
    attempts = 0

    while True:
        print("-----------------------------------------------")
        guess = input("Enter a number: ").strip()

        valid, message = validate_guess(guess)

        if not valid:
            print(message)
            continue

        attempts += 1
        bulls, cows = count_bulls_cows(secret, guess)

        print(format_result(bulls, cows))

        if bulls == DIGITS:
            print("Correct, you've guessed the right number")
            print(f"in {attempts} guesses!")
            print("-----------------------------------------------")
            print("That's amazing!")
            break


def main() -> None:
    """Start the Bulls and Cows game."""
    print_intro()
    secret = generate_secret_number()
    game_loop(secret)


if __name__ == "__main__":
    main()
