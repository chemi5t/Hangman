import random


word_list = ["Mango", "Banana", "Grapes", "Pear", "Lychee"] # Create 'word_list' of favorite fruits and check via print

class Hangman():

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list) # The word to be guessed, picked randomly from the word_list
        self.word_guessed = ['_' for _ in self.word] # i.e. If the word is 'apple', the word_guessed list would be ['', '', '', '', '']
        self.num_letters = len(set(self.word)) # num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
        self.num_lives = num_lives #num_lives: int - The number of lives the player has at the start of the game.
        self.word_list = word_list # word_list: list - A list of words.
        self.list_of_guesses = [] # list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially

    def check_guess(self, guess): # Take the guessed letter as an argument and checks if the letter is in the word randomly chosen by program.
        if guess in self.word: # checks if the guess is in the word
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if guess == letter: # Check if the letter is equal to the guess
                    self.word_guessed[i] = guess # Replace the corresponding "_" in word_guessed with the guess
            self.num_letters -= 1 # Reduce the number of unique letters by 1 after a correct guess
        else:
            self.num_lives -= 1 # Reduce `num_lives' by 1.
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            
    def ask_for_input(self): # ask the user until a vlaid letter given
        while True:
            guess = input("Please enter a single letter: ").lower()  # Convert guess to lowercase
            if len(guess) != 1 or not guess.isalpha():  # Check if the guess is a single alphabetical character
                print("Invaliad letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess) # add guess to list_of_guesses 
                # print("Good guess!")
                break 
        # check_guess(guess)

# ask_for_input()

person1 = Hangman(word_list)
person1.ask_for_input()
