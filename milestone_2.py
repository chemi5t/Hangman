import random


word_list = ["Mango", "Banana", "Grapes", "Pear", "Lychee"] # create 'word_list' of favorite fruits and check via print
# print(word_list)

def random_selection_from_word_list(): # randomly selects a fruit from 'word_list'
    word = random.choice(word_list)
    return word

print(random_selection_from_word_list()) # testing random_selection_from_word_list() function
print(random_selection_from_word_list())
print(random_selection_from_word_list())
print(random_selection_from_word_list())

def user_letter_selection(): # user to enter a single letter
    guess = input("Please enter a single letter: ").lower()  # Convert guess to lowercase
    if len(guess) == 1 and guess.isalpha(): # check length of guess is 1 character and that it is alphabetical
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

user_letter_selection()