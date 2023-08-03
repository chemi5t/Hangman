# Hangman - Project Documentation Guideline

> Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 1: Set up the environment

- Setting up of the dev environment. Covering the following prerequisites:
  1. Setting up
  2. Operating Systems
  3. What is the command line
  4. File Navigation & File Paths
  5. File Manipulation
- Setting up of GitHub

- Outcomes from Milestone 1: Prerequisites and setup of laptop and GitHub up successful. Now able to commence the project and save/track changes via Git and GitHub. VS Code to be used for writing the code.

## Milestone 2: Create the variables for the game

- Using Python commands such as if-else statements and while loops. Covering the following prerequisites:
  1. What is Python?
  2. Google Colab
  3. Variables
  4. Comments
  5. Numbers
  6. Strings
  7. Booleans
  8. Lists
- Task 1: Define a list of possible words. Create a file named milestone_2.py. This file contains the code for the first milestone.
- Further prerequisites:
  1. Package managers
  2. pip
  3. conda
  4. Dictionaries
  5. Tuples
  6. Sets
  7. Intro to Control Flow
  8. Imports
- Task 3: Ask the user for input.
- Task 4: Check that the input is a single character. Validate the input to ensure only a single letter is entered and that only alphabetical characters are provided by the user.
- Followed by prerequisite:
  1. Github README files
- Task 5: Start documenting experience. Upload files to the repository and create a README file. Add documentation to README file. Describe the code written in this milestone.
- Task 6: Update the latest code changes to GitHub.

- Outcomes from Milestone 2: Milestone 2 continues from Milestone 1. Prerequisites and tasks successfully completed for Milestone 2. Code saved to milestone_2.py, and README updated. In milestone_2.py, 'word_list' created with 5 different types of fruits; a function defined to randomly select a word from the 'word_list', and a function defined that allows a user to select a single alphabetical letter of choice. The local repository is backed up into GitHub. Find attached screenshots below of progress to date.

Repo created in GitHub with README.md file.
> ![Alt text](<MS2 screen shot of GitHub repo.jpg>)

Hangman code written using VS Code and saved as milestone_2.py and uploaded to GitHub.
> ![Alt text](<MS2 screen shot of VS Code.jpg>)

## Milestone 3: Check if the guessed character is in the word

- Prerequisite:
  1. For Loops, Iteration, and Control Flow Tricks
- Task 1: Iteratively check if the input is a valid guess. Code it so that it continuously asks the user for a letter and validates it. Create a new script called milestone_3.py.
- Task 2: Check whether the guess is in the word
- Prerequisite:
  1. Functions
- Task 3: Create a function to run the checks
- Task 4: Update documentations
- Task 5: Update latest code to GitHub

- Outcomes from Milestone 3: Milestone 3 continues from Milestone 2. Prerequisites and tasks successfully completed for Milestone 3. Functions created so far:
  1. def random_selection_from_word_list(): # randomly selects a fruit from 'word_list'
  2. def check_guess(guess): # takes the guessed letter as an argument and checks if the letter is in the word randomly chosen by the program.
  3. def ask_for_input(): # ask the user until a valid letter is given and then passed as an argument to 'check_guess(guess)'
Code saved to milestone_3.py, and README updated. Local repository backed up into GitHub. Find attached screenshots below of progress to date.

Hangman code written using VS Code and saved as milestone_3.py.
> ![Alt text](<MS3 screen shot of VS Code.jpg>)

## Milestone 4: Create the Game class

- Prerequisite:
  1. Error Handling with Control Flow 
  2. Context Managers
  3. Comprehensions
  4. Defining Functions
  5. Object-Oriented Programming
  6. Principles of OOP Design
  7. What is `self` in Python?
  8. Magic Methods
  9. Principles of OOP - Abstraction
  10. Principles of OOP - Encapsulation
  11. Principles of OOP - Inheritance
  12. Principles of OOP - Polymorphism
  13. Checks for code quality
  14. Docstrings
- Task 1: Create a new script called milestone_4.py. The code from the third milestone is copied into this. Define the init method of the Hangman class.

Create a class called Hangman. Pass in word_list and num_lives as parameters. Make num_lives a default parameter and set the value to 5.

Initialize the following attributes:

word: The word to be guessed, picked randomly from the word_list.

word_guessed: list - A list of the letters of the 'word', with "'_'" for each letter not yet guessed. For example, if the word is 'apple', the 'word_guessed' list would be ['', '', '', '', '']. If the player guesses 'a', the list would be ['a', '', '', '', ''].

num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.

num_lives: int - The number of lives the player has at the start of the game.

word_list: list - A list of words.

list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.
- Task 2: Create methods for running the checks that will ask the user to guess a letter and another method that will check if the guess is in the word. 
Create the check_guess method and pass the guess to the method as a parameter. Then define a method called ask_for_input.
- Task 3: Define what happens if the letter is in the word. 
The check_guess method is extended to replace the underscore(s) in the word_guessed with the letter guessed by the user.
- Task 4: Define what happens if the letter is NOT in the word - reduce `num_lives` by 1.
- Task 5: Update your documentation and update README. Define the class with the attributes and methods you created.
- Task 6: Update the latest code changes to GitHub

- Outcomes from Milestone 4: Milestone 4 continues from Milestone 3. Prerequisites and tasks successfully completed for Milestone 4. Class and functions created so far:
  1. class Hangman(): # Initialized and methods worked on
  2. def check_guess(self, guess): # Take the guessed letter as an argument and checks if the letter is in the word randomly chosen by the program.
  3. def ask_for_input(self): # Ask the user until a valid letter is given
Code checked against an instance of the class and work saved to milestone_4.py, and README updated. The local repository is backed up into GitHub. Find attached screenshots below of progress to date.

Hangman code written using VS Code and saved as milestone_4.py.
> ![Alt text](<MS4 screen shot of VS Code.jpg>)

## Milestone 5: Putting it all together

- Task 1: Putting it all together in a new script called milestone_5.py. Copy all the codes in milestone_4.py file into the newly created milestone_5.py file. Create a function that will run all the code to run the game as expected. 
- Task 2: Document your experience. Update the README.md file and explain how you defined the whole game and the logic behind it.
- Task 3: Update the latest code changes to GitHub. 

- Outcomes from Milestone 5: Milestone 5 continues from Milestone 4. Prerequisites and tasks successfully completed for Milestone 4. Additional function created to run the class Hangman:
  1. def play_game(word_list): # Function that plays the game
Code checked against an instance of the class. Code then debugged and work saved to milestone_4.py, and README updated. The local repository is backed up into GitHub. Find attached screenshots below of progress to date.

Hangman code written using VS Code and saved as milestone_4.py.
> ![Alt text](<MS5 screen shot of VS Code.jpg>)

## Conclusions

- This project exposes you to Python coding with emphasis on writing classes, methods, and object-oriented programming. In addition, you require the knowledge of using the command line, VS Code software, git for version control, and GitHub for backing up of work. 

- This project helps you reflect on the structure of code written for a task in logical steps. To be able to handle how data can be entered or interpreted to be entered. With checks in the code being put in place to account for any errors that may be inputted.

- The scope for the game can be expanded in a number of way. To list a few:

1. More words to guess from.
2. Give the option of themes to choose from which words may be guessed. 
3. Have AI extend your options for words.
4. A setting introduced to change the difficulty level of the game, i.e., longer words to guess.
5. Can create new rules where you are rewarded for consecutive correct guesses, i.e., life added onto your tally.
