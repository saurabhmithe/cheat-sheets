# Lists in Python are pretty powerful.
# Unlike strings, lists are mutable.

fruits = ['Apple', 'Banana', 'Strawberry', 'Cherry']

# They pretty much work like arrays in other languages.
print fruits[0]

# The elements of the list can be accessed using index.
second_fruit = fruits[1]
print second_fruit

# The indexes work pretty much the same way they work in strings including negative indexes.
last_fruit = fruits[-1]
print last_fruit

# Looping through lists is just as simple as the 'for each' loop in Java.
print 'All fruits ->'
for fruit in fruits:
    print fruit

# Adding new elements can be done through appending.
new_fruit = 'Mango'
fruits.append(new_fruit)
print fruits # This prints the whole list

# Lists can be dynamically constructed.
squares = [] # Declaring empty list.
for i in range(1, 11): # Range can be specified for looping like normal loops in other languages.
    squares.append(i ** 2) # The ** sign is used for exponents.
print squares

# Something that is unlike other languages is this.
cubes = [x**3 for x in range (1, 11)]
print cubes

# Just like you can slice a fruit, you can slice a list.
first_three_fruits = fruits[0:3]
print first_three_fruits

# Lists can be copied to other lists.
new_fruits = fruits[:] # You can use the indexes and get just a part of the list.
print new_fruits