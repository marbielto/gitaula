# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:36:48 2021

@author: MGB
"""

#Which of these metacharacters isn't to do with repetition?
#Result : \

#How many groups are in the regex (ab)(c(d(e)f))(g)?
import re
pattern = r"(ab)(c(d(e)f))(g)"
match = re.match(pattern, "abcdefg")
if match:
    print(len(match.groups()))
    
#Which regex would match "email@domain.com"?
# R: \w+@domain.com

#Which string would be matched by "[01]+0$"?
# R: 10101111001010

pattern = r"(4{5,6})\1"
# \1 means repetitions of the first group
# '4' * 5 = 44444 AND '4' * 6 = 444444
# make it twice of ('4' * 5 ) = 10 fours
# or twice of ('4' * 6) = 12 fours 

match  = re.match(pattern, "4444444444")
if match:
    print("Match 1")

match = re.match(pattern, "444444444444")
if match:
    print("Match 2")


"""
PROBLEM 
    Phone Number Validator


You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.

Sample Input
81239870

Sample Output
Valid
"""

number = input()
pattern = r"^[1|8|9][0-9]{7}$"
match = re.search(pattern, number)
if match:          
    print("Valid")
else:
    print("Invalid")

    


    