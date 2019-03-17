# While loops are as easy as they are powerful.
all_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)

length = len(all_numbers) # len() function lets you find the length of a data structure

i = 0
while i < length:
    print all_numbers[i]
    i += 1 # Compound increment operator


# An infinite loop can be operated using boolean True

i = 0
while True:
    if i > 20: # Without this condition, this loop will run forever
        break # break gets us out of the loop
    print i
    i += 1