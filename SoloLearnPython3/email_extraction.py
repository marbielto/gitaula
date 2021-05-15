# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 09:00:41 2021

@author: MGB
"""

import re 

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())
    
