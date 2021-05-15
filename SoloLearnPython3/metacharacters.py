# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 13:01:42 2021

@author: MGB
"""

"""
import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")
    
if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")
""" 
# metacharacters "^" and "$"
# The pattern "^gr.y$" means that the string
# should start with gr,
# then follow with any character, 
# except a newline, and end with y.

import re 

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stingray"):
    print("Match 3")
    