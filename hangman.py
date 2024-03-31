# Problem Set 2, hangman.py
# Name: Mikias Yohannes 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()

def initialize_game():
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    print("--------------")


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
        
    return True

    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
  
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "

    return guessed_word
            



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_available = ""
    letters = string.ascii_lowercase

    for letter in letters:
        if letter not in letters_guessed:
            letters_available += letter

    return letters_available
  
def get_user_guess():
  
  return input("Please guess a letter: ").lower()

def check_user_guess(user_guess: string, letters_guessed):
  
  if user_guess in get_available_letters(letters_guessed) and len(user_guess) == 1 or user_guess == "*":
    return True
  else:
    return False

def get_unique_letter_count(secret_word):
  
  unique_letter_count = 0
  letters_counted = []
  
  for letter in secret_word:
    if letter not in letters_counted:
      unique_letter_count += 1
      letters_counted.append(letter)
  
  return unique_letter_count


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    user_remaining_guesses = 6
    user_remaining_warnings = 3
    
    
    initialize_game()
    print("You have", user_remaining_warnings, "warnings left.")
    print("You have", user_remaining_guesses,"guesses left.")
    print("Available letters:", get_available_letters(letters_guessed))   
    
    while not is_word_guessed(secret_word, letters_guessed) and user_remaining_guesses > 0:
      user_guess = get_user_guess()
      
      if not check_user_guess(user_guess, letters_guessed) and len(user_guess) > 1:
        user_remaining_warnings -= 1
        if user_remaining_warnings < 0:
          print("Oops! Please guess one letter at a time. You have no warnings left so you lose on guess:", get_guessed_word(secret_word, letters_guessed))
          user_remaining_guesses -= 1
        else:  
          print("Oops! Please guess one letter at a time. You have", user_remaining_warnings, "warnings left.", get_guessed_word(secret_word, letters_guessed))
        
      elif not check_user_guess(user_guess, letters_guessed) and not user_guess.isalpha():
        user_remaining_warnings -= 1
        if user_remaining_warnings < 0:
          print("Oops! That is not a valid letter. You have no warnings left so you lose on guess:", get_guessed_word(secret_word, letters_guessed))
          user_remaining_guesses -= 1
        else:
          print("Oops! That is not a valid letter. You have", user_remaining_warnings, "warnings left.", get_guessed_word(secret_word, letters_guessed))
          
      elif not check_user_guess(user_guess, letters_guessed) and user_guess in letters_guessed:
        user_remaining_warnings -= 1
        if user_remaining_warnings < 0:
          print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess", get_guessed_word(secret_word, letters_guessed))
          user_remaining_guesses -= 1
        else:
          print("Oops! You've already guessed that letter. You have", user_remaining_warnings, "warnings left.", get_guessed_word(secret_word, letters_guessed))
      
      if check_user_guess(user_guess, letters_guessed):
        letters_guessed.append(user_guess)
        if user_guess in secret_word:
          print("Good guess:", get_guessed_word(secret_word, letters_guessed))   
        else: 
          if user_guess in ["a","e","i","o","u"]:
            user_remaining_guesses -= 2
          else:
            user_remaining_guesses -= 1
          print("Oops that letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
      
      if is_word_guessed(secret_word, letters_guessed):
        break
      
      print("-------------")
      available_guesses = get_available_letters(letters_guessed)
      print("You have", user_remaining_guesses, "guesses left.")
      print("Available letters:", available_guesses)
      
    if is_word_guessed(secret_word,letters_guessed):
      print("")
      print("Congratulations, you won!")
      total_score = user_remaining_guesses * get_unique_letter_count(secret_word)
      print("Your total score for this game is:", total_score)
    else:
      print("")
      print("Sorry, you ran out of guesses. The word was", secret_word)
      



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    
    if len(my_word) != len(other_word):
      return False
    else:
      for i in range(len(my_word)):
        if my_word[i] != '_' and my_word[i] != other_word[i] or my_word[i] != '_' and my_word.count(my_word[i]) != other_word.count(other_word[i]):
          return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    hints = ""
    num_of_matches = 0
    for word in wordlist:
      if match_with_gaps(my_word, word):
        hints += (word + " ")
        num_of_matches =+ 1
    
    if num_of_matches == 0:
      print("No matches found")
      
    print(hints)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    user_remaining_guesses = 6
    user_remaining_warnings = 3
    
    
    initialize_game()
    print("You have", user_remaining_warnings, "warnings left.")
    print("You have", user_remaining_guesses,"guesses left.")
    print("Available letters:", get_available_letters(letters_guessed))   
    
    while not is_word_guessed(secret_word, letters_guessed) and user_remaining_guesses > 0:
      user_guess = get_user_guess()
      
      if check_user_guess(user_guess, letters_guessed) and user_guess == "*":
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        continue
        
      if not check_user_guess(user_guess, letters_guessed) and len(user_guess) > 1:
        user_remaining_warnings -= 1
        if user_remaining_warnings < 0:
          print("Oops! Please guess one letter at a time. You have no warnings left so you lose on guess:", get_guessed_word(secret_word, letters_guessed))
          user_remaining_guesses -= 1
        else:  
          print("Oops! Please guess one letter at a time. You have", user_remaining_warnings, "warnings left.", get_guessed_word(secret_word, letters_guessed))
        
      elif not check_user_guess(user_guess, letters_guessed) and not user_guess.isalpha():
        user_remaining_warnings -= 1
        if user_remaining_warnings < 0:
          print("Oops! That is not a valid letter. You have no warnings left so you lose on guess:", get_guessed_word(secret_word, letters_guessed))
          user_remaining_guesses -= 1
        else:
          print("Oops! That is not a valid letter. You have", user_remaining_warnings, "warnings left.", get_guessed_word(secret_word, letters_guessed))
          
      elif not check_user_guess(user_guess, letters_guessed) and user_guess in letters_guessed:
        user_remaining_warnings -= 1
        if user_remaining_warnings < 0:
          print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess", get_guessed_word(secret_word, letters_guessed))
          user_remaining_guesses -= 1
        else:
          print("Oops! You've already guessed that letter. You have", user_remaining_warnings, "warnings left.", get_guessed_word(secret_word, letters_guessed))
      
      if check_user_guess(user_guess, letters_guessed):
        letters_guessed.append(user_guess)
        if user_guess in secret_word:
          print("Good guess:", get_guessed_word(secret_word, letters_guessed))   
        else: 
          if user_guess in ["a","e","i","o","u"]:
            user_remaining_guesses -= 2
          else:
            user_remaining_guesses -= 1
          print("Oops that letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
      
      if is_word_guessed(secret_word, letters_guessed):
        break
      
      print("-------------")
      available_guesses = get_available_letters(letters_guessed)
      print("You have", user_remaining_guesses, "guesses left.")
      print("Available letters:", available_guesses)
      
    if is_word_guessed(secret_word,letters_guessed):
      print("")
      print("Congratulations, you won!")
      total_score = user_remaining_guesses * get_unique_letter_count(secret_word)
      print("Your total score for this game is:", total_score)
    else:
      print("")
      print("Sorry, you ran out of guesses. The word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)