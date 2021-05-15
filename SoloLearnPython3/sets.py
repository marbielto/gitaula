# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:55:23 2021

@author: MGB
"""

"""
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)
"""

"""
letters = {"a", "b", "c", "d"}
if "e" not in letters:
    print(1)
else:
    print(2)
""" 
"""   
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

nums = {"a", "b", "c", "d"}
nums.add("z")
print(len(nums))
"""
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)


a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)
