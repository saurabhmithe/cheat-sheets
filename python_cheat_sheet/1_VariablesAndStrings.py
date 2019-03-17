# This is a comment in Python. It is a good practice to leave a space after the '#' symbol.

# Let's look at the variables. Variables don't need the type specifiers like other languages.
# Just as in Java, strings in Python are immutable.
message = 'Hello World!'
print message

# String variables can also be declared using single quotes ('') or double quotes ("").
first_name = 'Saurabh'
last_name = "Mithe"

# Concatenation works the same as some other languages using plus (+) symbol.
introduction = 'My name is ' + first_name + ' ' + last_name
print introduction

# The useful thing about being able to use different kinds of string quotes is the ability to use quotes without escaping.
# We will use a single quote (') as a part of the sentence without escaping it and it works just fine.
sentence = "This is a cheat sheet that I have prepared to help you get acquainted with Python's basic syntax and functions. "
print sentence

# Python not only allows you to add strings but also to multiply it, which is a neat trick if you ask me.
divider = '-' * 115
print divider

# Python provides some nifty tools to manipulate strings using index.
example = 'ThisIsAnUnnecessaryLongString'

# The first position would be the starting position and the next would be the ending position.
# Mind that the end index would be the index of the character after your intended last character.
# And the start index would be the index of the character you want to start with.
print example[8:19]

# You can also use negative index which would work exactly opposite.
print example[0] # This prints the first letter.
print example[-1] # This prints the last character.

# If you leave the start index blank, it would start from beginning.
# If you leave the end index blank, it would go all the way to the end.
print example[:19] # Started from the beginning.
print example[8:] # Went all the way to end.

# Of course it would work even when neither of the indexes are present.
print example[:] # Unnecessary but cool.

# Go ahead. Play with it. It's fun.

