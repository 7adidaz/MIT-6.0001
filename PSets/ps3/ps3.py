# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : abdallah elhdad
# Collaborators : none
# Time spent    : one day 

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
global score 
score = 0

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*' : 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n): # -----------D(o)N(e)----------
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    #word = word.lower()
#word = word.lower()
    product1 = 0
    product2 = 0
    if word == "":
        return 0
    else: 
        word = word.lower()
        for i in word:
            
            product1 += SCRABBLE_LETTER_VALUES[i]
        product2 = abs( (7 * len(word)) - (3 * ( n - len(word))))
        return product1 * product2



#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand): 
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = math.floor(n / 3)

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand["*"] = 1
    for i in range(num_vowels+1, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word): # -----------D(o)N(e)---------- 
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    handcopy = hand.copy()
    word= word.lower()
    for i in word:
        if i in handcopy:
            if handcopy[i]>1 :
                handcopy[i]-=1
            else:
                del handcopy[i]
    return handcopy


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list): # -----------D(o)N(e)----------
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    freq = {}
    starred = False
    for i in word:
        if i == "*":
            starred = True
            break
    if starred:
        newword = ''
        for j in VOWELS:
            for i in word:
                if i == "*":
                    newword += j
                else:
                    newword += i
            if newword in word_list:
                return True
            newword = ''
        return False
    else:
        for i in word:
            freq[i] = freq.get(i, 0) + 1
            if i not in hand:
                return False
        for i in freq.keys():
            if freq[i] > hand[i]:
                return False
        if word in word_list:
            return True
        else:
            return False
    

            
        

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand): # -----------D(o)N(e)----------
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    count = 0
    if hand == {}:
        return count 
    else: 
        for i in hand.keys():
            count +=hand[i]
    return count


def play_hand(hand, word_list): # -----------D(o)N(e)----------
    """
    
    
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    global score
    currentscore=0
    totalscore =0
    handcopy = hand.copy()
    userinput = ''  
    while True:
        if calculate_handlen(handcopy) > 0:
            
            print("Current Hand:")
            display_hand(handcopy)
            userinput = input("Enter word, or !! to indicate that you are finished:")
            if userinput == "!!":
		score += totalscore
                print("Total score:", totalscore, "points")
                break
            else:
                if is_valid_word(userinput, handcopy, word_list):
                    currentscore = get_word_score(userinput, calculate_handlen(handcopy))
                    totalscore += get_word_score(userinput, calculate_handlen(handcopy))
                    print('-', userinput, '-', "earned",currentscore, ", Total:", totalscore, "points")
                else:
                    ## ------ last modifiation ------ ##
                    
                    if (calculate_handlen(handcopy) - len(userinput)) > 0:
                        print("That is not a valid word. Please choose another word.")
                    else:
                        print("That is not a valid word.")
        else:
            print("Ran out of letters. Total score for this hand:", totalscore, "points")
            score += totalscore
            break
        handcopy = update_hand(handcopy, userinput)
        
    print("__________________________________")
                
                
            

#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter): # -----------D(o)N(e)----------
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    valid = ''
    for i in string.ascii_lowercase:
        if i not in hand.keys():
            valid += i
    y = random.choice(valid)
    savedvalue = hand[letter]
    del hand[letter]
    hand[y] = savedvalue
    return hand


def play_game(word_list): # -----------D(o)N(e)----------
    """
    Allow the user to play a series of hands
    
    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    global score
    num_of_hands = int(input("Enter total number of hands:"))
    yes = ["yes", "y", "ok"]
    while num_of_hands>0:
        hand = deal_hand(HAND_SIZE)
        print("Current Hand:")
        display_hand(hand)
        firsttime = True
        if firsttime:
            sub = input("Would you like to substitute a letter?")
            sub = sub.lower()
            if sub in yes:
                found = True
                while found:
                    letter = input("Which letter would you like to replace:")
                    if letter in hand:
                        substitute_hand(hand, letter)
                        found =False
                        break
                    else: 
                        print("Letter not in hand")
        play_hand(hand, word_list)
        replay = input("Would you like to replay the hand?")
        if replay in yes:
            play_hand(hand, word_list)
            num_of_hands-=1
        else:
            num_of_hands-=1
    print("Total score over all hands:",score)
            
        
    
    
    
    # handsnumber = int(input ("Enter total number of hands:"))
    # totalscore =0
    # while handsnumber > 0:
    #     hand = deal_hand(HAND_SIZE)
    #     lasthand = hand
        
    #     play_hand(hand, word_list)




## a j e f * r x
## {'a' : 1,'j' : 1,'e' : 1,'f' : 1,'*' : 1, 'r' : 1,'x' : 1}
## a c f i * t x
## {'a' : 1,'c' : 1,'f' : 1,'i' : 1,'*' : 1, 't' : 1,'x' : 1}
## u e * b v d q 
## {'u' : 1,'e' : 1,'*' : 1,'b' : 1,'v' : 1, 'd' : 1,'q' : 1}
#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    ## -------------------------testing section-------------------------
    ##play_hand({'u' : 1,'e' : 1,'*' : 1,'b' : 1,'v' : 1, 'd' : 1,'q' : 1} ,word_list)
    play_game(word_list)
