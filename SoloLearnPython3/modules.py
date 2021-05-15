#modules
'''
import random
for i in range(5):
	value = random.randint(1,6)
	print(value)
'''
"""
from math import pi
print(pi)
"""
'''
how import more than one
from math import sqrt, cos
'''
"""
from math import sqrt as square_root
print(square_root(100))
"""
"""
def print_nums(x):
	for i in range(x):
		print(i)
		return
print_nums(10)
"""
'''
def func(x):
	res=0
	for i in range(x):
		res += i
	return res
print(func(4))
'''

#problem celsius to fahrenheit

celsius = int(input())

def conv(c):
    #your code goes here
    c = ((9/5) * celsius) + 32
    return c
fahrenheit = conv(celsius)
print(fahrenheit)