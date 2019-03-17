# Tuples are similar to lists except for the fact that they are immutable.
# Just so that we are able to tell them apart, the clever Python creators
# used round brackets '(' for tuples as opposed to square brackets '[' for lists.

tuple = ('new york', 'chicago', 'austin', 'san jose')

# Just like lists and strings, tuples can be concatenated and sliced.
first_two = tuple[0:2]
print first_two

# Tuples can be accessed using index.
print tuple[3]

# Since tuples are immutable, we cannot update a tuple directly but
# we can create other tuples using existing tuple.
cars = ('mercedes', 'audi', 'bmw', 'ferrari', 'aston martin')

# cars[0] = 'porsche' This is an invalid operation.

# But we can use values from the existing tuple and concatenate it with a tuple containing our desired value.
# We will create a new tuple with just one value 'porsche'
# But to create a tuple with a single value, we would need to add a comma after the value just like I did here.

# This is an invalid operation since 'porsche' will be treated as string and you cannot concatenate a string with a tuple.
#new_cars = ('porsche') + cars[1:] Not valid.


new_cars = ('porsche',) + cars[1:] # Valid (notice the comma).
print new_cars

# Just as addition, deleting a value from a tuple is not possible.
# You can, however, explicitly delete an entire tuple using del operator.
del new_cars
# print new_cars # Not valid. new_cars does not exist.

# The looping and other operations can be performed in the same way as lists.
primes = (2, 3, 5, 7, 11, 13, 17)
for i in primes:
    print i