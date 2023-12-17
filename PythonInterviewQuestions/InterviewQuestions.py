# What is the difference between List and Tuple?
# What is the difference between a Set and Dictionary?
# What is the difference between Python Arrays and lists?
# What is List Comprehension? Give an Example.
# What is Dictionary Comprehension? Give an Example
# What is a lambda function?
# What is zip and enumerate in Python?
# What are *args and *kwargs?
# What is a break, continue, and pass in Python? 
# What is the difference between a shallow copy and a deep copy?
# What are Decorators?
# What are Iterators in Python?
# What are Generators in Python?
# What are Pickling and Unpickling?
# What is __init__() in Python?
# What are Python namespaces?
# What is self in Python?
# How will you capitalize the first letter of string?
# What is map function in Python?
# How to combine dataframes in pandas?
# What is the difference between merge, join and concat function in pandas?
# What is the difference between pop & remove function in list?
# What is the use of .join operator?
# write a program to print if a number is odd or even?
# what is inheritance in python and how it is used?
# what is multithreading and multiprocessing in python?
# How is memory managed in python?
# what is the purpose of __main__?

number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")


# We have a list of cities ['new york city', 'mountain view', 'chicago', 'los angeles']. Write a program to print the cities as a string seperated by next line.

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities: #city is the iteration variable, and cities is 
                    #the iterable being looped over
    print(city)
print("Done!")

# Write a program to print only the odd number till 20.

for i in range(1,10,2):
    print(i)

# Write a program to print cities in capitals. use .title()

# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())


cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()

print(cities)


# List Comprehensions


cities=['chennai','bangalore','mumbai']
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

capitalized_cities = [city.title() for city in cities]

# givn a dictionary print a list of names whose score is more than 65

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)


