# Hangman - Project Documentation Guideline

> (Include here a brief description of the project, what technologies are used etc.)
> 
> Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 1: Set up the enviroment

- Setting up of the dev enviroment. Covering the following prerequisites:
  1. Setting up
  2. Operating Systems
  3. What is the command line
  4. File Navigation & File Paths
  5. File Manipulation
- Setting up of GitHub
  
- (Answer some of these questions in the next few bullet points. What have you built? What technologies have you used? Why have you used those?)
- (Example: The FastAPI framework allows for fast and easy construction of APIs and is combined with pydantic, which is used to assert the data types of all incoming data to allow for easier processing later on. The server is ran locally using uvicorn, a library for ASGI server implementation.)
  
```python
"""Insert your code here"""
```

> Insert an image/screenshot of what you have built so far here.

## Milestone 2: Create the variables fo the game

- Using Python commands such as if-else statments and while loops. Covering the following prerequisites:
  1. What is Python?
  2. Google Colab
  3. Variables
  4. Comments
  5. Numbers
  6. Strings
  7. Booleans
  8. Lists
- Task 1: Define a list of posisble words. Create a file named milestone_2.py. This file contains the code for the first milestone. In this task, we are creating a list of words.
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
- Task 5: Start documenting experience. Upload files to the repository and creat a README file. Add documentation to README file. Describ the code written in this milestone.
- Task 6: Updat the lastest code changes to GitHub. Upload the latest code changes from your local project repository to GitHub. To do so, first add your changes to the staging area and make a commit. Finally, push the changes to GitHub.


- (Does what you have built in this milestone connect to the previous one? If so explain how. What technologies are used? Why have you used them? Have you run any commands in the terminal? If so insert them using backticks (To get syntax highlighting for code snippets add the language after the first backticks).)

- (Example below:)

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

- (The above command is used to check whether the topic has been created successfully, once confirmed the API script is edited to send data to the created kafka topic. The docker container has an attached volume which allows editing of files to persist on the container. The result of this is below:)

```python
"""Insert your code here"""
```

> Insert screenshot of what you have built working.
> 
> "C:/Users/chemi/hangman_project/MS2 screen shot of GitHub repo.jpg"
> 
> "C:\Users\chemi\hangman_project\MS2 screen shot of GitHub repo.jpg"

## Milestone 3: Check if the guessed character is in the word

- Prerequisite:
  1. For Loops, Iteration and Control Flow Tricks
- Task 1: Iteratively check if the input is a valid guess. Code it so that it continuously ask the user for a letter and validates it. Create a new script called milestone_3.py.
- Task 2: Check whether the guess is in the word
- Prerequisite:
  1. Functions
- Task 3: Creat a function to run the checks
- Task 4: Update documentions
- Task 5: Update latest code to GitHub
- Functions created so far:
  1. def random_selection_from_word_list(): # randomly selects a fruit from 'word_list'
  2. def check_guess(guess): # takes the guessed letter as an argument and checks if the letter is in the word randomly chosen by program.
  3. def ask_for_input(): # ask the user until a vlaid letter given and then passed as argument to 'check_guess(guess)'

## Milestone 4: Create the Game class

- Prerequisite:
  1. Error Handling with Control Flow 
  2. Context Managers
  3. Comprehensions
  4. Defining Functions
  5. Object Oriented Programming
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

Initialise the following attributes:

word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.

word_guessed: list - A list of the letters of the word, with for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. If the player guesses 'a', the list would be ['a', '', '', '', ''].

num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.

num_lives: int - The number of lives the player has at the start of the game.

word_list: list - A list of words.

list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.
- Task 2: Create methods for running the checks that will ask the user to guess a letter and another method that will check if the guess is in the word.

Create the check_guess method and pass the guess to the method as a parameter. Then define a method called ask_for_input.
- Task 3: Define what happens if the letter is in the word. 

Check_guess method is extended to replace the underscore(s) in the word_guessed with the letter guessed by the user.
- Task 4: Define what happens if the letter is NOT in the word - reduce `num_lives' by 1.
- Task 5: Update your documentation and update README. Define the class with the attributes and methods you created.
- Task 6: Update the latesr code changes to GitHub

## Milestone n

- (Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.)

- (Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!)

## Conclusions

- (Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.)

- (Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?)
