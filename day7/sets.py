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


# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error.
# The clear() method empties the set:


# The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x) #apple
