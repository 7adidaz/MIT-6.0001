# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.message_text = text
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        vDic = {'a' :vowels_permutation[0],
                'e' :vowels_permutation[1],
                'i' :vowels_permutation[2],
                'o' :vowels_permutation[3],
                'u' :vowels_permutation[4],
                }
        dic = {
         'a': 'a',
         'b': 'b',
         'c': 'c',
         'd': 'd',
         'e': 'e',
         'f': 'f',
         'g': 'g',
         'h': 'h',
         'i': 'i',
         'j': 'j',
         'k': 'k',
         'l': 'l',
         'm': 'm',
         'n': 'n',
         'o': 'o',
         'p': 'p',
         'q': 'q',
         'r': 'r',
         's': 's',
         't': 't',
         'u': 'u',
         'v': 'v',
         'w': 'w',
         'x': 'x',
         'y': 'y',
         'z': 'z',
         'A': 'A',
         'B': 'B',
         'C': 'C',
         'D': 'D',
         'E': 'E',
         'F': 'F',
         'G': 'G',
         'H': 'H',
         'I': 'I',
         'J': 'J',
         'K': 'K',
         'L': 'L',
         'M': 'M',
         'N': 'N',
         'O': 'O',
         'P': 'P',
         'Q': 'Q',
         'R': 'R',
         'S': 'S',
         'T': 'T',
         'U': 'U',
         'V': 'V',
         'W': 'W',
         'X': 'X',
         'Y': 'Y',
         'Z': 'Z'
         }
        for i in dic.keys():
            if i in 'aeiou':
                dic[i] =  vDic[i]
            elif i in 'AEIOU':
                dic[i] =  vDic[i.lower()].upper()
        return dic
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        message = self.get_message_text()
        decrypted_message =''
        for i in message:
            if i in string.ascii_letters:
                decrypted_message += transpose_dict[i]
            else: 
                decrypted_message+=i
        return decrypted_message
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        encrypted = SubMessage(self.message_text)
        possiablecompinations = get_permutations('aeiou')
        counter1 = 0 
        solved = ''
        
        for i in range(120):
            
            counter0 = 0
            
            vowels_permutation = possiablecompinations[i]
            
            trans_dic = encrypted.build_transpose_dict(vowels_permutation)
            
            trying_decrebting = encrypted.apply_transpose(trans_dic)
            
            splited = trying_decrebting.split(' ')
            
            
            for w in splited:
                
                if is_word(self.valid_words, w):
                    
                    counter0 +=1
                    
            if counter0 > counter1:
                
                counter1 = counter0
                
                solved = trying_decrebting
                
        return solved

if __name__ == '__main__':

    # Example test case
    # message = SubMessage("Hello World!")
    # permutation = "eaiuo"
    # enc_dict = message.build_transpose_dict(permutation)
    # print("Original message:", message.get_message_text(), "\nPermutation:", permutation)
    # print("Expected encryption:", "Hallu Wurld!")
    # print("Actual encryption:", message.apply_transpose(enc_dict))
    
    # enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    # print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    
    
    # -------------Test Case One -------------- 
    message = SubMessage("Abdallah loves shopping!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "\nPermutation:", permutation)
    print("Expected encryption:", "Ebdelleh luvas shupping!")
    print("Actual encryption:  ", message.apply_transpose(enc_dict))
    
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    
    