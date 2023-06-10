import random

# List of words to choose from
word_list = ["hangman", "python", "github", "code", "programming"]

def get_random_word():
    """Returns a random word from the word list."""
    return random.choice(word_list)

def display_hangman(tries):
    """Displays the hangman ASCII art based on the number of tries left."""
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def play_hangman():
    word = get_random_word().lower()
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    print("Guess the word before the hangman is complete.")

    while tries > 0:
        # Display hangman and guessed letters
        print(display_hangman(6 - tries))
        print()

        # Display word with underscores for unguessed letters
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)
        print()

        if "_" not in display_word:
            print("Congratulations! You guessed the word:", word)
            return

        # Prompt for user input
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            tries -= 1
            print("Incorrect guess. Tries left:", tries)

        print()

    print("You lost! The word was:", word)

play_hangman()
