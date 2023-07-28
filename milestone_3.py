import random


word_list = ["Mango", "Banana", "Grapes", "Pear", "Lychee"] # create 'word_list' of favorite fruits and check via print
# print(word_list)

def random_selection_from_word_list(): # randomly selects a fruit from 'word_list'
    word = random.choice(word_list)
    return word

word = random_selection_from_word_list()


'''

The ask_for_input function.

Step 1. Define a function called ask_for_input.

Step 2. Move the code that you wrote in the Iteratively 
check if the input is a valid guess task into this function 
block.

Step 3. Outside the while loop, but within this function, 
call the check_guess function to check if the guess is in 
the word. Don't forget to pass in the guess as an argument 
to the method.

Step 4. Outside the function, call the ask_for_input function to test your code.'''

def check_guess(guess):
    if guess in list(word): # checks if the guess is in the word
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(): # ask the user until a vlaid letter given
    while True:
        guess = input("Please enter a single letter: ").lower()  # Convert guess to lowercase
        if len(guess) == 1 and guess.isalpha():  # Check if the guess is a single alphabetical character
            # print("Good guess!")
            return guess  # I chose Return over "Break" to get out of the loop if the guess is valid
        else:
            print("Invaliad letter. Please, enter a single alphabetical character.")
    
        check_guess(guess)

    

# guess = user_letter_selection() # assigned output of 'user_letter_selection()' to variable 'guess'

ask_for_input()
