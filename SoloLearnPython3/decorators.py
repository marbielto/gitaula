# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:59:46 2021

@author: MGB
"""

#Decor can be call this way
"""
def decor(func):
    def wrap():
        print("==========")
        func()
        print("==========")
        
    return wrap


def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()
"""

#Or this way
"""
def decor(func):
    def wrap():
        print("==========")
        func()
        print("==========")
        
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text()
"""



