import pickle as pkl

# takes objects and converts them into a binary string
# this is called as serializing or pickling (Python)
# it also allows converting the binary strings back to objects

# wb for write in binary
file = open('test.pickle', 'wb')
person = {'first_name': 'John', 'last_name': 'Smith'}
man = {'a': 'x', 'b':'y'}
pkl.dump(person, file)
pkl.dump(man, file)
file.close()

# rb for read binary
file = open('test.pickle', 'rb')
person = pkl.load(file)
print(person)
man = pkl.load(file)
print(man)

