import random

words = ["dog", "cat", "moose", "spider", "rat", "mouse", "bunny", "fish", "human", "grass", "flower", "yellow", "red", "orange", "green", "scream"]

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word(words)
    guessed_letters = set()
    attempts = 5
    print("Welcome to Hangman!")
    print(f"You have {attempts} attempts to guess the word.")
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        guess = input("Guess a letter: ").lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            print(f"Lives remaining: {attempts}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
