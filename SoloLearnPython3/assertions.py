#Assertions

"""
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)
"""

"""
temp = -10
assert (temp >= 0), "Colder than absolute zero!"
"""

#Opening Files
"""
myfile = open("teste.txt")
"""

"""
#write code
myfile = open("teste.txt", "w")

#read code
myfile = open("teste.txt", "r")
myfile = open("teste.txt")

#binary write mode
myfile = open("teste.txt", "wb")
"""


"""
file = open("teste.txt", "w")
file.close()
"""

#Reading Files
"""
file = open("teste.txt", "r")
cont = file.read()
print(cont)
file.close()
"""


"""
file = open("teste.txt", "r")
print(file.read(2))
file.close()
"""

"""
file = open("teste.txt", "r")
for i in range(21):
  print(file.read(4))
file.close()
"""

"""
file = open("teste.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()
"""

file = open("teste.txt", "r")
print(file.readlines())
file.close()

file = open("teste.txt", "r")

for line in file:
    print(line)
file.close()

#Writing files
"""
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()
"""

'''
file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()
'''

msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

