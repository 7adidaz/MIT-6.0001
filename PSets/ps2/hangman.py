# Problem Set 2, hangman.py
# Name:
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
import math

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


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ''
    for i in secret_word:
        if i in letters_guessed:
            result += i
        else:
            result += '_ '
    return result


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_of_letters_deleted = ''
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            list_of_letters_deleted += i
    return list_of_letters_deleted


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings = 3
    guesses = 6
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings, "warnings left.")

    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):

        # is_word_guessed(secret_word, letters_guessed)
        print("------------------------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        userinput = input("Please guess a letter:")

        if not userinput.isalpha():
            warnings -= 1
            if warnings >= 0:
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses -= 1
                print("Oops! That is not a valid letter. you have no warnings left so you lose one guess")
        else:
            userinputlowerd = userinput.lower()
            if userinputlowerd in letters_guessed:
                if warnings >= 1:
                    warnings -= 1
                    print("Oops! You've already guessed that letter. You have", warnings, "warnings left:",
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                          get_guessed_word(secret_word, letters_guessed))
                    guesses -= 1

            else:
                letters_guessed.append(userinputlowerd)
                if userinputlowerd in secret_word:
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                else:
                    print("Oops! That letter is not in my word.", get_guessed_word(secret_word, letters_guessed))
                    if userinputlowerd in ['a', 'e', 'i', 'o']:
                        guesses -= 2
                    else:
                        guesses -= 1
    print("------------------------------")
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is:", secret_word_uniq(secret_word) * guesses)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)


def secret_word_uniq(secret_word):
    stx = secret_word
    used = []
    for s in stx:
        if s not in used:
            used.append(s)
    return len(used)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = []
    used = []
    for char in my_word:
        # print("char :", char)
        if char != '_' and char != " ":
            if char not in used:
                letters.append(char)
                used.append(char)

    guess_len = len(letters) + math.ceil(((len(my_word) - len(letters)) / 2))
    # print("guess len :", guess_len)
    if guess_len != len(other_word):
        return False

    else:
        if my_word != get_guessed_word(other_word, letters):
            return False

        else:
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return_list = []
    nopos = "$"
    for i in wordlist:
        if match_with_gaps(my_word, i):
            return_list.append(i)
    if len(return_list) > 0:
        return return_list
    else:
        return nopos


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    global guess
    warnings = 3
    guesses = 6
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings, "warnings left.")

    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):

        # is_word_guessed(secret_word, letters_guessed)
        print("------------------------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        userinput = input("Please guess a letter:")
        if userinput == '*':
            print("Possible word matches are:")
            for i in show_possible_matches(get_guessed_word(secret_word, letters_guessed)):
                if i[0] != "$":
                    print(i)
                else:
                    print("No matches found")
        else:
            if not userinput.isalpha():
                warnings -= 1
                if warnings >= 0:
                    print("Oops! That is not a valid letter. You have", warnings, "warnings left:",
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    guesses -= 1
                    print("Oops! That is not a valid letter. you have no warnings left so you lose one guess")
            else:
                userinputlowerd = userinput.lower()
                if userinputlowerd in letters_guessed:
                    if warnings >= 1:
                        warnings -= 1
                        print("Oops! You've already guessed that letter. You have", warnings, "warnings left:",
                              get_guessed_word(secret_word, letters_guessed))
                    else:
                        print(
                            "Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                            get_guessed_word(secret_word, letters_guessed))
                        guesses -= 1

                else:
                    letters_guessed.append(userinputlowerd)
                    if userinputlowerd in secret_word:
                        print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                    else:
                        print("Oops! That letter is not in my word.", get_guessed_word(secret_word, letters_guessed))
                        if userinputlowerd in ['a', 'e', 'i', 'o']:
                            guesses -= 2
                        else:
                            guesses -= 1
        guess = get_available_letters(letters_guessed)
    print("------------------------------")
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is:", secret_word_uniq(secret_word) * guesses)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

# print(show_possible_matches("a_ _ l_ "))
# print(show_possible_matches("t_ _ t"))
if __name__ == "__main__":

    """
        to play hangman without hints
        uncomment the section marked with stares
        
        to play hangman with hints
        comment the section marked with and mark
    """
    secret_word = choose_word(wordlist)
    # ******************************************
    # hangman(secret_word)
    # ******************************************
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    hangman_with_hints(secret_word)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
