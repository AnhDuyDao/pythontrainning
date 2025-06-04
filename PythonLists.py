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

# Change list item values
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert more items than index
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert less items than index
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert item at specific index
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)