#!/usr/bin/env python3

"""
This file contains a set of python challenges with my solutions. 
The challenges are divided into different categories:
---- Warmup, Level 1, Level 2
Note:
All challenging problems were obtained from Pierian-Data/Complete-Python-3-Bootcamp
No outside or Pierian-Data solutions were used to solve each challenging problem
"""
#-----------------------------------------------------------
#                       WarmUp Section
#-----------------------------------------------------------

# PROBLEM 1 - LESSER OF TWO EVENS 
"""
Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater 
if one or both numbers are odd
"""

def lesser_of_two_evens(a,b):
    if a < b and a % 2 == 0 and b % 2 == 0: #even
        return a 
    elif b < a and a % 2 == 0 and b % 2 == 0:   #even
        return b
    elif a < b and a % 2 != 0 and b % 2 == 0: # a<b and a is odd and b is even
        return b
    elif a < b and a % 2 == 0 and b % 2 != 0:   #a<b and a is even and b is odd
        return b
    elif a < b and a % 2 != 0 and b % 2 != 0:   #a<b both a and b are off
        return b
    elif b < a and a % 2 != 0 and b % 2 == 0:   # b<a and a is odd and b is even
        return a
    elif b < a and a % 2 == 0 and b % 2 != 0:   # b<a and a is odd and b is even
        return a
    elif b < a and a % 2 != 0 and b % 2 != 0: # b<a and a is odd and b is even
        return a

lesser_of_evens  = lesser_of_two_evens(3,1)
print(lesser_of_evens)

# PROBLEM 2 - ANIMAL CRACKERS
"""
Write a function that takes a two-word string and return True if both words begin with se same letter
"""

def animal_cracker(text):
    #Placeholder variable
    two_strings  = text.split() #convert the two-word string into a list
    #print(two_strings)

    if two_strings[0][0] == two_strings[1][0]: #calling specific indexes
        return True
    else:
        return False 

print(animal_cracker('hello houses'))

# PROBLEM 3 - MAKES TWENTY
"""
Given two integers, return True if the sum of the integers is 20, or if one of the integers is 20
If not, return false 
"""

def makes_twenty(n1,n2):
    #placeholder variable
    sum_of_numbers = n1 + n2 

    if sum_of_numbers == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False
print(makes_twenty(2,20))

#-----------------------------------------------------------
#                       Level 1 Problems 
#-----------------------------------------------------------

# PROBLEM 4 - OLD MACDONALD
"""
Write a function that capitalizes the first and fourth letters of a name
"""

def old_macdonald(name):
    #placeholder variables
    outputstring = ''

    for position,letter in enumerate(name): #enumarating allows to reference each letter at a specific location of the string array
        if position == 0:
            outputstring += letter.upper()
        elif position == 3:
            outputstring += letter.upper()
        else:
            outputstring += letter
    return outputstring
print(old_macdonald('macdonald'))

# PROBLEM 5 - MASTER YODA
"""
Given a sentence, return a sentence with the words reversed
"""
def master_yoda(yodasentence):
    #placeholder variable
    list_string = yodasentence.split() #converts a string into a list
    empty_string = " "                 #used to join a string to a list to add a whitespace between words
    yoda_true_sentence_list = []        #this will hold the list of string already reversed
    yoda_true_sentence = ''             #output string

    for yoda_words in reversed(list_string):                                #reverse method reversed a list
        yoda_true_sentence_list.append(yoda_words)
        yoda_true_sentence = empty_string.join(yoda_true_sentence_list)     #.join allows to convert a list into a string and adds a whitespace between the words
    return yoda_true_sentence
print(master_yoda('We are ready'))

# PROBLEM 6 -- ALMOST THERE 
"""
Given an integer n, return True if n is within 10 of either 100 or 200
"""

def almost_there(n):
    
    if n > 80 and n < 111:
        return True
    elif n > 189 and n < 211:
        return True
    else:
        return False
print(almost_there(205))

#-----------------------------------------------------------
#                       Level 2 Problems 
#-----------------------------------------------------------

# PROBLEM 7 -- FIND 33
"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
"""
def has_33(nums): 
    #placeholder variable 
    length_of_list = len(nums) #used to determine while loop comparison
    the_number_list = []

    #While loop iteration number
    i = 0

    for the_number in nums:                 #this for loop creates a copy list of all the nums
        the_number_list.append(the_number)
    #print(the_number_list)
   
    while i < length_of_list: #while loop is used to be able to reference to a specific location in the arrays

        if nums[i] == 3:    #first must check if the number is 3
            #print("num is three")
            if nums[i] == the_number_list[i-1] or nums[i] == the_number_list[i+1]: #compare the number with the copy list and see if there's a three before or after
                #print("is a double")
                return True
            elif nums[i] != the_number_list[i-1] or nums[i] != the_number_list[i+1] :
                print("not a double")
        elif nums[i] != 3:
            continue
        else:
            pass

        i += 1
print(has_33([1,2,3,3,4,7,3,4,3,3]))

#   PROBLEM 8 -- PAPER DOLL
"""
Given a string, return a string where for every character in the original there are three characters
"""

def paper_doll(DollSentence):
    this_doll_sentence = ''
    for every_doll_letter in DollSentence:
        this_doll_sentence += every_doll_letter * 3 #each token can be multiplied
    return this_doll_sentence
print(paper_doll('Hello'))

# PROBLEM 9 --- BLACKJACK
"""
Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum
If their sum exceeds 21 and there's an eleven, reduce the sum by 10
If the sum after adjustment exceeds 21, return 'BUST'
"""
def blackjack(g,h,j):
    result5 = ''
    sum_of_cards = g + h + j

    if sum_of_cards <= 21:
        return sum_of_cards
    elif sum_of_cards > 21 and 11 in (g,h,j): # it's interesting that in python you can do this comparison. Range checker
        sum_of_cards = sum_of_cards - 10

        if sum_of_cards > 21:
            result5 = 'BUSTED'
            return result5
        else:
            return sum_of_cards       
    else:
        print("idk")

print(blackjack(11,30,4))