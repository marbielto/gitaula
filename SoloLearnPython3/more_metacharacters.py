# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:43:25 2021

@author: MGB
"""

import re
# metacharacter * means "zero or more occurences"
"""
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")
"""

# metacharacter + means "one or more occurences"
"""
pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1")

if re.match(pattern, "gggggggggggggggggggg"):
    print("Match 2")

if re.match(pattern, "abc"):
    print("Match 3")
"""
# metacharacter ? means "zero or one repetitions"
"""
pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match 1")

if re.match(pattern, "icecream"):
    print("Match 2")

if re.match(pattern, "sausages"):
    print("Match 3")

if re.match(pattern, "ice--ice"):
    print("Match 4")
"""
# to match both 'color' and 'colour'

## pattern = r"colo(u)?r"
    
    
#Curly Braces

##"9{1,3}$" matches string that have 1 to 3 nines.

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print("Match 1")

if re.match(pattern, "999"):
    print("Match 2")
    
if re.match(pattern, "9999"):
    print("Match 3")
