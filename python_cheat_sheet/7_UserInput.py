# You can read user input pretty easily in python.
your_name = raw_input("what's your name?") # You can provide inline prompt to user.
print your_name

your_age = raw_input("what's your age?")
print your_age

cities = {'san jose' : 'CA', 'boulder' : 'CO', 'phoenix' : 'AZ', 'austin' : 'TX'}
print cities.keys()
favorite_city = raw_input("what's your favorite city?")
print 'Your favorite city is located in \n' # /n is for newline
print cities[favorite_city]