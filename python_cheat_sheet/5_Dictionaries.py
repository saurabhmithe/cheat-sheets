# A dictionary in Python is something that lets you hold key-value pairs.
# To keep things simple, dictionaries have curly braces '{' to set them apart from lists and tuples.
home = {'name':'Earth', 'planet_number':3}

# Values can be accessed using the key
print home['name']
print home['planet_number']

# Dictionaries are mutable. So it is perfectly valid to do something like this.
home['name'] = 'Mars' # If Elon is right, we need to move fast.
home['planet_number'] = 4

# This is what our future would look like.
print home['name']
print home['planet_number']

# Looping is a bit different in dictionaries.
# Since we have two values per entry, we can specifiy two variables while looping.
months = {1:'January', 2:'February', 3:'March', 4:"April", 5:'May', 6:'June', 7:'July'}
for number, name in months.items(): # We are using items() function since we need both keys and values
    print str(number) + '  ' + name

for month in months.values(): # We are using just values here
    print month

for i in months.keys(): # We can even iterate over keys
    print months[i]