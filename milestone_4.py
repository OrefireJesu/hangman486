import random


class Hangman:

    def __init__(self, word_list, num_lives = 5):
        # self.word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry']
        # self.word = random.choice(word_list)
        # self.word_guessed = ['_'] * len(self.word)
        # self.num_letters = len(set(self.word))
        # self.num_lives = num_lives
        # self.list_of_guesses = []

        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()  # Pick a random word
        self.word_guessed = ['_'] * len(self.word)  # Initialize with underscores
        self.num_letters = len(set(self.word))  # Count unique letters
        self.list_of_guesses = []  # List to track guessed letters

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            self.num_letters = self.num_letters - 1
        else: 
            self.num_lives = self.num_lives -1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
                    
       
    def ask_for_input(self):
        while(True):
            guess = input("Enter a single letter: ")  
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                print("TESTR")
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


# Testing the class
if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "grape"]
    game = Hangman(word_list)
    game.ask_for_input()

# word_list = ["apple", "banana", "cherry", "grape"]
# game = Hangman(word_list)

# game.ask_for_input()