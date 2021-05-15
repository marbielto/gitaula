# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:05:03 2021

@author: MGB
"""

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

#Dictionaries
"""
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
"""


#KeyError
"""
primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}

print(primary["red"])
print(primary["yellow"])
"""

#TypeError
"""
bad_dict = {
    [1,2, 3]: "one two three",
}
"""

#Dictionary Functions
"""
squares = {1: 1, 2:4, 3:"error", 4:16,}
squares[8] = 64
squares[3] = 9
print(squares)
"""

"""
primes = {1:2, 2:3, 4:7, 7:17}
print(primes[primes[4]])
"""

"""
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
"""

"""
pairs = {1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
"""

fib = {1:1, 2:1, 3:2, 4:3}
print(fib.get(4,0) + fib.get(7,5))
