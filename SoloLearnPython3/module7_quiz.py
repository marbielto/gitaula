# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:39:19 2021

@author: MGB
"""
"""
nums = {1,2,3,4,5,6}
nums = {0,1,2,3} & nums
nums = filter(lambda x: x>1, nums)
print(len(list(nums)))
"""
"""
def power(x,y):
    if y==0:
        return 1
    else:
        return x * power(x,y-1)
print(power(2,3))


a = (lambda x: x * (x+1))(6)
print(a)

nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x%2==0, nums))
print(res)

var = (3 - 2)
print(var)



thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

"""

n=int(input()) 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
      return fibonacci(n-1)+fibonacci(n-2)
for n in range(n):
   print(fibonacci(n))