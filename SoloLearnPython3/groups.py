# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:42:13 2021

@author: MGB
"""
#A group can be created by surrounding part
# of a regular expression with parentheses.
import re
"""
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")
"""
"""
pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())
"""    

# exercise 1
# What would group(3) be of
# a match of 1(23)(4(56)78)9(0)?
"""
pattern = r"1(23)(4(56)78)9(0)"

match = re.match(pattern, "12345678901934")
if match:
    print(match.group(3))
"""

# named groups anda non-capturing groups
"""
pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())    
"""    
# exercise 2
#What would be the result of len(match.groups()) 
#of a match of (a)(b(?:c)(d)(?:e))
"""    
pattern = r"(a)(b(?:c)(d)(?:e))"

match = re.match(pattern, "abcde")
if match:
    match = len(match.groups())
    print(match)
"""

# Another important metacharacter | means "or"
pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print("Match 1")
    
match = re.match(pattern, "grey")
if match:
    print("Match 2")

match = re.match(pattern, "griy")
if match:
    print("Match 3")
