# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:51:52 2021

@author: MGB
"""

"""
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
"""

#longest word
text = input().split()
print(text)
length = [len(x) for x in text]
maximum = max(length)
text_index = length.index(maximum)
print(text_index)
print(text[text_index])
