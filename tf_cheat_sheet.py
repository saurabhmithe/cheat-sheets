import tensorflow as tf

# Constants
# Cannot change the values of constant
a = tf.constant(2.0, tf.float32)
b = tf.constant(3.0)

# Variables
# Variables can be changes in value
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b

# Placeholders
# Used for feeding the data from outside
a = tf.placeholder(tf.float32)
b = a * 2

# Session is run to evaluate the nodes
# TensorFlow object is an empty graph
# Everything in TF is an operation
# You write the operations but they are only run during a session
with tf.Session() as sess:
    # feed data from outside
    result = sess.run(b, feed_dict={a:3.0})

# Running a session
a = tf.constant(5.0)
b = tf.constant(3.0)
c = a * b # Create a graph

# Launch Session
sess = tf.Session()

# Evaluate the tensor c
print(sess.run(c)) # This is where a * b will be performed

# this is a variable
zero = tf.Variable(0)

# this is a constant
one = tf.constant(1)

new_value = tf.add(zero, one)

# changing the variable value
update = tf.assign(zero, new_value)

# when you have variables, you need to do the initialization
init_op = tf.global_variables_initializer()

# create and run the session
sess = tf.Session()
sess.run(init_op)  # run init operation
sess.run(zero)

for _ in range (5):
    sess.run(update)
    print(sess.run(zero))

# strings
hello = tf.constant("hello")
world = tf.constant("world")
hello_world = tf.add(hello, world)
print(sess.run(hello_world))

# placeholders
a = tf.placeholder(tf.float32)  # a placeholder for 32-bit float
b = a * 2 # multiply the content of a by 2
result = sess.run(b, feed_dict={a:3})  # populate a with 3
print(result)
result = sess.run(b, feed_dict={a: [3, 4, 5]})  # passing a tensor
print(result)
dict = {a:[[1, 2, 3], [4, 5, 6], [7, 8, 9]]}
result = sess.run(b, feed_dict=dict)
print(result)

sess.close()

# another way of using session
# using a with block, session closes automatically
with tf.Session() as sess:
    result = sess.run(hello_world)
    print(result)

# get a handle of the graph using this method
# every node in the graph is an operation
graph = tf.get_default_graph()
graph.get_operations()

a = tf.constant(10, name='a') # name this operation as a
operations = graph.get_operations()
print(operations)

b = tf.constant(20, name='b')
operations = graph.get_operations()
print(operations)

c = tf.add(a, b, name='c')
operations = graph.get_operations()
print(operations)

d = tf.multiply(a, b, name='d')
operations = graph.get_operations()
print(operations)

# executing the graph
with tf.Session() as sess:
    result = sess.run(c)
    print(result)
    operations = graph.get_operations()
    print(operations)

    result = sess.run(d)
    print(result)
    operations = graph.get_operations()
    print(operations)

