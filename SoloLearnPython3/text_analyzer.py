# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:07:17 2021

@author: MGB
"""
"""
filename = input("Enter a filename: ")

with open(filename) as f:
    text = f.read()

print(text)
"""

#count char function

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

filename = input("Enter a filename: ")

with open(filename) as f:
    text = f.read()

print(count_char(text, "A"))


for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc,2)))
    
