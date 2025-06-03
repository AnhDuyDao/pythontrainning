thislist = ["apple", "banana", "cherry"]
print(thislist)

# Changeable
# Allows duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List length
print(len(thislist))

# List items - Data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# Mixed data types
list4 = ["apple", 1, True]

# List constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # Output: banana
print(thislist[-1]) # Output: cherry (last item)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
