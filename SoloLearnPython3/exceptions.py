#Exceptions
"""
num1 = 7
num2 = 0
print(num1/num2)
"""

#Exception Handling
"""
try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occured")
    print("due to zero division")
"""

"""
try:
    var = 10
    print(10/2)
except ZeroDivisionError:
    print("Error")
print("Finished")
"""

"""
try:
    variable = 10
    print(variable + "hello")
    print(variable /2)
except ZeroDivisonError:
    print("Divided by zero")
    
except (ValueError, TypeError):
    print("Error ocurred")
"""

"""
try:
    word = "spam"
    print(word/0)
except:
    print("An error occurred")
"""

#finally
"""
try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")
"""

"""
try:
    print(1)
    print(10/0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed last")
"""

#Raising Exceptions
"""
print(1)
raise ValueError
print(2)
"""

"""
name = "123"
raise NameError("Invalid name!")
"""

try:
    num = 5/0
except:
    print("An error occured")
    raise
