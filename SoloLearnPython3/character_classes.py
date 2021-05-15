# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:11:05 2021

@author: MGB
"""

import re
"""
pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")
"""

"""
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern , "E3"):
    print("Match 2")

if re.search(pattern, "1ab"):
    print("Match 3")
"""   

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1")
    
if re.search(pattern, "AbCdEfG123"):
    print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")

pattern = r"[^0-9]"

if re.search(pattern, "Hi there!"):
    print("Match 4")