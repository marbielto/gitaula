# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:56:48 2021

@author: MGB
"""

import re

pattern = r"(.+)\1"

match = re.match(pattern, "word word")
if match:
    print("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print("Match 2")

match = re.match(pattern, "abc code")
if match:
    print("Match 3")
    
    
# useful special sequences \d, \s and \w
# digits, whitespace and word characters
"""
pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")

if match:
    print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern, "! $?")
if match:
    print("Match 3")
"""

# \b matches the empty string between \w and \W characters
# or \w characters an the begining or end of the string
#It represents the boundary between words
pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
    print("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
    print("Match 2")

match = re.search(pattern, "We scattered.")
if match:
    print("Match 3")

    