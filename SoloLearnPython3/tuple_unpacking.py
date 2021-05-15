# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:46:36 2021

@author: MGB
"""

numbers = (1, 2, 3)
a, b, c = numbers
#print(a)
#print(b)
#print(c)


x,y=[1,2]
x,y = y,x
#print(x,y)

#A variable that is prefaced with
#an asterisk (*) takes all values from the iterable
#that are left over from the other variables.
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
print(a)
print(b)
print(c)
print(d)
"""

a,b,c,d,*e,f,g=range(20)
print(len(e))