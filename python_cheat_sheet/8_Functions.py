# Functions are defined with the keyword def.

def add(a, b):
    """This method adds two numbers"""
    # The above string is called as docstring that can be used
    # to demonstrate how the use the function and what it does.
    return a + b

print add(2, 3)

# Python functions can return multiple values.
def get_details(city):
    # We will be using nested dictionaries here.
    database = {"san jose" : {'state' : 'CA', 'population' : 40000}, "detroit" : {'state' : 'MI', 'population' : 85000}}
    requested_city = city
    city_details = database[city]
    requested_city_state = city_details['state']
    requested_city_population = city_details['population']

    # Returning all three parameters.
    return requested_city, requested_city_state, requested_city_population

city, state, population = get_details("san jose")
print city
print state
print population

# Functions allow you to define default values in case one or more of the values are not provided by user.
def bake_pizza(crust='wheat', toppings = ('pepperoni', 'bacon')):
    print 'Baking a pizza with ' + crust + ' crust and ' + str(toppings) + ' toppings.'

bake_pizza('italian bread', ('tomato', 'spinach', 'mushrooms')) # all the inputs
bake_pizza() # no inputs
bake_pizza('whole wheat') # partial inputs

