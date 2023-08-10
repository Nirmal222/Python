# Python Datatypes
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

#Getting the Data Type
x = 5
print(type(x))

x = "Hello"  # string type (str)
x = 2 # integer type (int)
x = 3.14 # float type (float)
x = ["1","2","3"] # list type (list)
x = ("1","2","3") # tuple type (tuple)
x = { "a":1, "b":2 } #dictionary (dict)
x = { "a", "b", "c" } # set type (set)
x = fronzenset({ "a", "b", "c" }) # frozenset type (frozenset)
x = true # boolean type (bool)
x = b"hello" #(bytes)


# Numbers
# Random Number
import random
print(random.randrange(1,10)) # Prints number between 1 to 9

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)