# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Dictionaries cannot have two items with the same key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
# -------------------------------

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# There is also a method called get() that will give you the same result:
x = thisdict.get("model")

# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys() 

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
    # dict_keys(['brand', 'model', 'year'])
    # dict_keys(['brand', 'model', 'year', 'color'])

# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()

# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


# To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
