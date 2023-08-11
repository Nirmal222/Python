# slicing strings 
name = "nirmal Kumar"
print(name[7:12]) # Kumar
# Slice from start 
print(name[:6]) # nirmal
# slice to end
print(name[7:])
# Negative indexing
print(name[-5:])
# -------------------------

# String Modifications
# Upper case 
upper = name.upper()
print(upper,'upper')
# lower case 
lower = name.lower()
print(lower,"lower")
# remove whitespace 
a = "Hello, World! "
print(a.strip(), "White space is removed at the end")
# replace string 
print(a.replace("H","J"))
# split string 
print(a.split(",")) # returns ["Hello", "World!"]
# -------------------------

# String concatenation 
s1 = "Hello"
s2 = "world"
concat = s1+s2
print(concat)
# -------------------------

age = 36
txt = "My name is Nirmal, I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# I want to pay 49.95 dollars for 3 pieces of item 567
# -------------------------

# Escape characters 
"""
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

To fix this problem, use the escape character \":
"""
txt = "We are the so-called \"Vikings\" from the north."
# We are the so-called "Vikings" from the north.


# usefull string methods 
str = "hello"
str.capitalize() # Hello
# count()	Returns the number of times a specified value occurs in a string
# find()	Searches the string for a specified value and returns the position of where it was found/ in operator does the same job
# isnumeric()	Returns True if all characters in the string are numeric
# replace()	Returns a string where a specified value is replaced with a specified value 

