# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:44:27 2021

@author: MGB
"""

# a list comprehension
"""
cubes = [i**3 for i in range(5)]
print(cubes)

nums = [i*2 for i in range(10)]
print(nums)
"""

#if
"""
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

a = [ i for i in range(20) if i%3==0 ]
print(a)
"""

#MemoryError
"""
even = [2*i for i in range(10**100)]
print(even)
"""

