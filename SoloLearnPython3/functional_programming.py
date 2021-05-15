# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:52:59 2021

@author: MGB
"""

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5 

print(apply_twice(add_five, 10))

def test(func, arg):
    return func(func(arg))

def mult(x):
    return x * x
print(test(mult,2))