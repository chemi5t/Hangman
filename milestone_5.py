import random


word_list = ["Mango", "Banana", "Grapes", "Pear", "Lychee"] # Create 'word_list' of favorite fruits and check via print

class Hangman():

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list # word_list: list - A list of words.
        self.num_lives = num_lives
        self.word = random.choice(self.word_list) # The word to be guessed, picked randomly from the word_list
        self.word_guessed = ['_' for _ in self.word] # i.e. If the word is 'apple', the word_guessed list would be ['', '', '', '', '']
        self.num_letters = len(set(self.word.lower())) # num_letters: int - The number of UNIQUE letters in the word (adjusted all to lowercase) that have not been guessed yet.
        self.num_lives = num_lives #num_lives: int - The number of lives the player has at the start of the game.
        self.list_of_guesses = [] # list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially

    def check_guess(self, guess): # Take the guessed letter as an argument and checks if the letter is in the word randomly chosen by program.
        if guess in self.word.lower(): # checks if the guess is in the word
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(self.word):
                if guess == letter.lower(): # Check if the letter is equal to the guess
                    self.word_guessed[i] = guess # Replace the corresponding "_" in word_guessed with the guess
            print(self.word_guessed)
            print(f"You have {self.num_lives} lives left.")
            self.num_letters -= 1 # Reduce the number of unique letters by 1 after a correct guess
        else:
            self.num_lives -= 1 # Reduce `num_lives' by 1.
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            print(self.word_guessed)
            
    def ask_for_input(self): # ask the user until a vlaid letter given
        while True:
            guess = input("Please enter a single letter: ").lower()  # Convert guess to lowercase
            if len(guess) != 1 or not guess.isalpha():  # Check if the guess is a single alphabetical character
                print("Invaliad letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                # print(self.list_of_guesses, f"; Guessed, {guess}.")
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(f"List of guesses: {self.list_of_guesses}") # add guess to list_of_guesses 
                break 

def play_game(word_list): # Function that plays the game
    num_lives = 5 # number of lives player has
    game = Hangman(word_list, num_lives) # Instance of Hangman class created
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was '{game.word}'.") # Once you have 0 lives, you have lost
            break
        elif num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!") # End of game
            break
        else:
            if game.num_letters > 0:
                game.ask_for_input() # Cycles back into the game asking for a new guess

play_game(word_list)