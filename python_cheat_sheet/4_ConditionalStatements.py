# Yes you can impose conditions in Python.
x = 12
y = 24

if x < y:
    print True # This is a boolean constant. Must start with uppercase letter.
else:
    print False

if x == y: # Comparision operator.
    print True
else:
    print False

if x <= 2*y: # Compound comparision.
    print True
else:
    print False

# Python has a handy way of dealing with lists.
primes = [2, 3, 5, 7, 11, 13, 17]

if 3 in primes: # Check whether an element is present in the list
    print True

if 9 not in primes: # Negation works equally well.
    print True

# Else if ladder works as obvious. We just use the keyword 'elif' for some reason.
month = 3
if month == 1:
    print 'January'
elif month == 2:
    print 'February'
elif month == 3:
    print 'March'

