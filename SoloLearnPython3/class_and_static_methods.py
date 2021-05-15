# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:38:08 2021

@author: MGB
"""
#Class method
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)
    
square = Rectangle.new_square(5)
print(square.calculate_area())
"""

#Static methods
"""
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        
    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True
        
ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
"""    
    
