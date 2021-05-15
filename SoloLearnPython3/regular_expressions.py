# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:51:24 2021

@author: MGB
"""

import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")
#function re.search and re.findall    
if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")
    
print(re.findall(pattern, "eggspamsausagespam"))

#methods group, start, end and span on match

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
    
    
#Search & Replace
str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

num = "079875498356"
pattern = r"9"
num = re.sub(pattern, "0", num)
print(num)