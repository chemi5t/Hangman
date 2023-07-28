import random


word_list = ["Mango", "Banana", "Grapes", "Pear", "Lychee"] # create 'word_list' of favorite fruits and check via print

def random_selection_from_word_list(): # randomly selects a fruit from 'word_list'
    word = random.choice(word_list)
    return word

word = random_selection_from_word_list() # word selected at random by function

def check_guess(guess): # takes the guessed letter as an argument and checks if the letter is in the word randomly chosen by program.
    if guess in word: # checks if the guess is in the word
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
     

def ask_for_input(): # ask the user until a vlaid letter given
    while True:
        guess = input("Please enter a single letter: ").lower()  # Convert guess to lowercase
        if len(guess) == 1 and guess.isalpha():  # Check if the guess is a single alphabetical character
            print("Good guess!")
            break # return guess  # I chose Return over "Break" to get out of the loop if the guess is valid
        else:
            print("Invaliad letter. Please, enter a single alphabetical character.")
    check_guess(guess)
    
ask_for_input()
