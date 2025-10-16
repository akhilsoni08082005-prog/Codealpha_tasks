import random

def hangman():
    # List of possible words
    words = ["python", "developer", "computer", "science", "hangman", "program"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("🎯 Welcome to Hangman!")
    print("Guess the word, one letter at a time.\n")

    while attempts > 0:
        # Display current word state
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())

        # Check if player guessed all letters
        if all(letter in guessed_letters for letter in word):
            print("🎉 Congratulations! You guessed the word:", word)
            break

        # Ask user for input
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")
        else:
            print("✅ Good guess!")

    else:
        print("\n💀 Game Over! The word was:", word)

# Run the game
hangman()