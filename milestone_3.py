import random


word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry']
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! {guess} is in the word.")
    else:
        print("Sorry, {guess} is not in the word. Try again.")
    
def ask_for_input():
    while(True):
        guess = input("Enter a single letter: ")  
        if len(guess) == 1 & guess.isalpha():
            check_guess(guess)
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()