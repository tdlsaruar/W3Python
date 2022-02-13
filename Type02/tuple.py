# Tuples are used to sotore multiple itmes in a single variable 
tup=('saruar','using','tuple')
print(tup)
# note tuple items are ordered unchangeable 
# tuple items are indesed, the first item has index[0]
# the seoncd items has indes[1]
# etc 
# Remember its unchangeable very very important for next step 
tup1=('here ',3,'three ')
print(len(tup1))
mytup=('new','more')
print(type(mytup))

# Update tuples 
# you know tuples are immutable which mean changeable simple man
xz=('here',234,234)
# here converting tuple to list 
y=list(xz)
print(y)
# xz.append('some')
# print(xz)
# you know tuple unchangeable so you can't append something or pop bcz it's tuple
# we cannot remove items in a tuple *****

# tuple loop 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# joint 2 tuple 
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# if you wanna multiply the content of a tuple a giive numbver of times you can use the * operatior 
hello=('no','have fun')
multiply=hello*3
print(multiply)
# here is tupple mathod 
# count() returns the number of times a specified value occurs in a tuple 
# indes() Searches the tuple fo a specified value and returns the postion of where it was round 
# that's all about tuple yaah hoo alhamdulilah i did this 
