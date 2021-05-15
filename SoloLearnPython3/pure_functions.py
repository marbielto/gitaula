# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:06:31 2021

@author: MGB
"""

#pure function
def pure_function(x,y):
    temp = x + 2*y
    return temp / (2*x + y)

#impure function
some_list = []

def impure(arg):
    some_list.append(arg)
    
