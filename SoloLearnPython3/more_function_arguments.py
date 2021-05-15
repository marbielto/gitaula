# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:44:31 2021

@author: MGB
"""

#varying number of arguments *args
def function(named_arg, *args):
    print(named_arg)
    print(args)
    
function(1, 2, 3, 4, 5)

#default values

def function(x, y, food="spam"):
    print(food)

function(1, 2)
function(3, 4,"egg")


def function(x, y,number="7"):
    print(number)

function(1, 2)

# **kwargs (standing of keyword arguments)

def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

