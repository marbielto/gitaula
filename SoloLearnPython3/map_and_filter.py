# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:01:56 2021

@author: MGB
"""

# map
"""
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

result = list(map(lambda x: x+5, nums))
print(result)
"""

# filter
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)