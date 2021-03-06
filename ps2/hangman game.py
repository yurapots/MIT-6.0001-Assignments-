# Hangman Game
# -----------------------------------
# helper code

import random
import string

WORDLIST_FILENAME = "words.txt"

# ____
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
# ----

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# ----

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    list_yes_no=[]
    for letter in secret_word:
        if letter in letters_guessed:
            list_yes_no.append(1)
        else:
            list_yes_no.append(0)
            break
    return 0 not in list_yes_no
# ----

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word=""
    for letter in secret_word:
        if letter in letters_guessed:
            word+=letter
        else:
            word+="_ "
    return word
# ----

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    allletters=string.ascii_lowercase
    availableletters=""
    for letter in allletters:
        if letter not in letters_guessed:
            availableletters+=letter
    return availableletters

consonants="bcdfghjklmnpqrstvwxyz"

vowels="aeiou"

# end of helper code
# -----------------------------------
# HANGMAN GAME


def hangman():
    wordlist=load_words()
    secret_word=choose_word(wordlist)
    letters_guessed=[]
    print("Welcome to Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long")
    nguesses=6 #This line sets the number of guesses to 6
    warnings=3 #This line sets the number of guesses to 3
    while nguesses>=1:
        print("You have", nguesses, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        userletter=(str.lower(str(input("Please guess a letter: ")))) #user input
        if str.isalpha(userletter): #did the user input a letter(not a number or a special character)?
            if userletter in letters_guessed: #has the letter already been guessed before?
                if warnings>=1: #dont lose a guess, lose one warning
                    warnings-=1
                    print("This letter has already been guessed before. You have",warnings,"warnings left:",get_guessed_word(secret_word, letters_guessed))
                else: #lose a guess
                    nguesses-=1
                    print("This letter has already been guessed before. You lose a guess:",get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(userletter)
                if userletter in secret_word: #is the letter in the secret word?
                    print("Good guess!", get_guessed_word(secret_word, letters_guessed))
                else:
                    if userletter in consonants: #wrong consonant, user loses 1 guess
                        nguesses-=1
                        print("Oops! That letter is not in the word:", get_guessed_word(secret_word, letters_guessed))
                    else: #wrong vowel, lose 2 guesses because there is less vowels than consonants so vowels are easier to guess
                        nguesses-=2
                        print("Oops! That letter is not in the word:", get_guessed_word(secret_word, letters_guessed))

        else:#the user entered an invalid input
            if warnings==0: #lose a guess if no more warnings left
                #lose a guess
                nguesses-=1
                print("That is not a letter. You lose a guess. 0 warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:#warning, don't lose a guess
                warnings-=1
                print("That is not a letter.", warnings, " warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("_"*20)
        isitguessed=is_word_guessed(secret_word, letters_guessed)#has the word been guessed?
        if isitguessed:
            score=nguesses*len(set(secret_word))#score=remaining number of guesses*number of unique letters in the secret word
            break#exit the while loop
    if isitguessed:#congratulate the user
        print("Congratulations! You guessed the word:", secret_word)
        print("Score:",score)
    else:#user lost
        print("You ran out of guesses. The word was:",secret_word)

# -----------------------------------

def matchword(word1, word2):
    #two words of equal length
    listlet=[]
    for i in range (len(word1)):
        if word1[i]==word2[i] or word1[i]=="_":
            listlet.append(1)
    return len(listlet)==len(word1)



#
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    modified_myword=""
    for letter in my_word:
        if letter !=" ":
            modified_myword+=letter
    if len(modified_myword)!=len(other_word):
        return False
    else:
        return matchword(modified_myword,other_word)



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    possiblewords=[]
    for word in wordlist:
        if match_with_gaps(my_word,word):
            possiblewords.append(word)
    if len(possiblewords)==0:
        print("No possible matches found")
    else:
        print("Possible matches are:",possiblewords)



def hangman_with_hints(secret_word):
    '''
    * If the guess is the symbol *, prints out all words in wordlist that
      matches the current guessed word.
    '''
    letters_guessed=[]
    print("Welcome to Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long")
    nguesses=6 #This line sets the number of guesses to 6
    warnings=3 #This line sets the number of guesses to 3
    while nguesses>=1:
        print("You have", nguesses, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
        userletter=(str.lower(str(input("Please guess a letter: ")))) #user input
        if str.isalpha(userletter): #did the user input a letter(not a number or a special character)?
            if userletter in letters_guessed: #has the letter already been guessed before?
                if warnings>=1: #dont lose a guess, lose one warning
                    warnings-=1
                    print("This letter has already been guessed before. You have",warnings,"warnings left:",get_guessed_word(secret_word, letters_guessed))
                else: #lose a guess
                    nguesses-=1
                    print("This letter has already been guessed before. You lose a guess:",get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(userletter)
                if userletter in secret_word: #is the letter in the secret word?
                    print("Good guess!", get_guessed_word(secret_word, letters_guessed))
                else:
                    if userletter in consonants: #wrong consonant, user loses 1 guess
                        nguesses-=1
                        print("Oops! That letter is not in the word:", get_guessed_word(secret_word, letters_guessed))
                    else: #wrong vowel, lose 2 guesses because there is less vowels than consonants so vowels are easier to guess
                        nguesses-=2
                        print("Oops! That letter is not in the word:", get_guessed_word(secret_word, letters_guessed))

        elif userletter=="*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:#the user entered an invalid input
            if warnings==0: #lose a guess if no more warnings left
                #lose a guess
                nguesses-=1
                print("That is not a letter. You lose a guess. 0 warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:#warning, don't lose a guess
                warnings-=1
                print("That is not a letter.", warnings, " warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("_"*20)
        isitguessed=is_word_guessed(secret_word, letters_guessed)#has the word been guessed?
        if isitguessed:
            score=nguesses*len(set(secret_word))#score=remaining number of guesses*number of unique letters in the secret word
            break#exit the while loop
    if isitguessed:#congratulate the user
        print("Congratulations! You guessed the word:", secret_word)
        print("Score:",score)
    else:#user lost
        print("You ran out of guesses. The word was:",secret_word)

wordlist=load_words()
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)