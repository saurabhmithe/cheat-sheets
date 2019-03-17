# Classes are required to construct objects.
class Dog():
    """Class for representing Dog"""

    # This is a constructor.
    # The self variable is the instance of the object itself.
    # While most of the languages keep this parameter hidden, Python needs you to specify it explicitly.
    # The double underscores (_) are used to indicate to compiler that this is a special method.
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print "Hello. My name is " +  self.name + "."


my_dog = Dog('Fluffy')
my_dog.introduce()