# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:02:15 2021

@author: MGB
"""

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)
'''    
def infinite_sevens():
    while True:
        yield 7

for i in infinite_sevens():
    print(i)
'''

"""
def numbers(x):
    for i in range(x):
        if i%2 == 0:
            yield i
print(list(numbers(11)))
"""

def make_word():
    word = ""
    for ch in "spam":
        word +=ch
        yield word
print(list(make_word()))