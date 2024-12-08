import random


class Hangman:

    def __init__(self, word_list, num_lives = 5):
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_'] * len(self.word) 
        self.num_letters = len(set(self.word)) 
        self.list_of_guesses = [] 

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
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

    def play_game(self, word_list):
        num_lives = 5
        game = Hangman(word_list, num_lives)
        while(True):
            if num_lives == 0:
                print('You lost!')
            elif self.num_letters > 0:
                self.ask_for_input()
            else:
                print('Congratulations. You won the game!')
                

word_list = ["apple", "banana", "cherry", "grape"]
game = Hangman(word_list)
game.play_game(word_list)