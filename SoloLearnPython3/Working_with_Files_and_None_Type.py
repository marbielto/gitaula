# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:58:06 2021

@author: MGB
"""
#Working with Files


"""
try:
    f = open("teste.txt")
    print(f.read())
finally:
    f.close()
    
with open("teste.txt") as f:
    print(f.read())


file = open("books.txt", "r")
print(file.readlines())


file.close()    
"""


"""
file = open("books.txt", "r")

for line in file:
	title=line.replace('\n','')
	count=len(title)
	print('{}{}'.format(title[0], count))
file.close()
"""

#More Types, None
"""
None == None
True
print(None)

def some_func():
    print("Hi!")

var = some_func()
print(var)
"""

"""
foo = print()
if foo == None:
    print(1)
else:
    print(2)
"""

 