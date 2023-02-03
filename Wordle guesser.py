# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 01:18:49 2022

@author: gansa001
"""

import numpy as np

# Produces a list of all uppercase strings from the .txt file.

all_words = [x.upper() for x in np.loadtxt("words.txt", dtype = str)]
all_words.sort()

Continue = input("Was your guess right?\nEnter 'Y' for yes and 'N' for no\n").upper()
if Continue == "Y":
    print("\nCONGRATS!!! 🎉")
    
while Continue == 'N':
    
    # get all wrong letters
    greys=str.upper(input('''Type exclusively grey letters.
If you typed two O's and only one is greyed out do not include an O.
Hit enter if none: '''))
    
    
    # get yellow letters
    yellows = str.upper(input('Type yellow letters with corresponding index.\nEg.S1D3 implies S is wrong\
in index 1 and D is wrong in index 3.\nHit enter if none: '))
    
    yellow_letters=[]
    yellow_index=[]
    for i in range(len(yellows)):
        if i%2==0:
            yellow_letters.append(yellows[i])
        else:
            yellow_index.append(int(yellows[i]))
            
            
    #get green letters
    greens = str.upper(input('Type green letters with corresponding index.\nEg.S1D3 implies S is correct\
in index 1 and D is correct in index 3.\nHit enter if none: '))
    
    green_letters=[]
    green_index=[]
    for i in range(len(greens)):
        if i%2==0:
            green_letters.append(greens[i])
        else:
            green_index.append(int(greens[i]))
            
            
    #remove all words that have the wrong letters
    all_words2=[]
    
    for word in all_words:
        for letter in greys:
            if word.__contains__(letter):
                all_words2.append(word)
                
    for i in all_words2:
        if i in all_words:
            all_words.remove(i)
            
    #remove all words that have do not have the correct letters in correct position
    for (letter,index) in zip(green_letters,green_index):
        new_words_green=[]
        for word in all_words:
            if letter in word:
                if word[index]==letter:
                    new_words_green.append(word)
        all_words=list(dict.fromkeys(new_words_green))
        
        
    #remove all words that have the correct letters in wrong position
    for (letter,index) in zip(yellow_letters,yellow_index):
        new_words_yellow=[]
        for word in all_words:
            if letter in word:
                if word[index]!= letter:
                    new_words_yellow.append(word)
        all_words=list(dict.fromkeys(new_words_yellow))
    
    #show available words to make next guess
    print(all_words)
    input('Press enter after making your guess')
    Continue = input("Was your guess right?\nEnter 'Y' for yes and 'N' for no\n").upper()
    if Continue == "Y":
        print("\nCONGRATS!!! 🎉")
