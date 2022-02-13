# List itmes are ordere, changeable,and allow duplicate values 
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
# list double round-brackets []
list5=['appple','mango','nothing']
print(list5[-1])
print(list5[::-1])
var=['car','bike','cycel']
print(var[2::])
var1=['have','has','do','does']
print(var1[2:3])

# Change list items 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# use the append() method to append an item: 
this=['march','may','boom']
this.append('sauar[0]')
print(this)

more=['nice ','to','meet']
this.append(more)
print(this)

# the pop() basically use for remove something from list 
pop1=['hello','pop','nice']
pop1.pop(0)
print(pop1)

# clear () tipically use for banish eleiment from list 
saruar=['tdl','he','is ',234,23]
print(saruar.clear())

# loop list print all items in the list ,one by one
for1=['no','yes ','may']
for x in for1:
    print(x)

# list comprehension you can do all taht with only one lie of code 
cricket=['moeen','sakib','all rounder']
for x in cricket:
 if 'a' in x:
    print(cricket)
# note for saruar you need to uderstand for while function to understand list comprehension go and rivise then try to lean this 
# now i am copying you are code then i will try here myself 


# ................................... mine
fruits=['x','orange','banana']

wlist = [x if x != "banana" else "orange" for x in fruits]


# Make a copy of a list with me copy()
co=['saruar','you',23]
new=co.copy()
print(new)
# Append list2 into list1 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Python has a set of built in methods that you can use on list here all list collected for rivistion 

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list