# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 20:44:23 2021

@author: MGB
"""

'''
from itertools import count

for i in count(3):
    print(i)
    if i >=11:
        break
    '''


from  itertools import accumulate, takewhile, chain

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x : x<= 6, nums)))
print(list(chain(nums)))


from itertools import takewhile

nums = [2, 4, 6, 7, 9, 8]

a = takewhile(lambda x: x%2==0, nums)
print(list(a))

from itertools import product, permutations
letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))


from itertools import product
a = {1,2}
print(len(list(product(range(3), a))))
print(list(product(range(3), a)))

