# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed

# * Note: Set items are unchangeable, but you can remove items and add new items.

# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
# A set can contain different data types: 


# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)  

# Once a set is created, you cannot change its items, but you can add new items. 
# To add one item to a set use the add() method. 

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# To add items from another set into the current set, use the update() method. 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.). 
