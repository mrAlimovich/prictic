''' Comprehension
    (1) What is Comprehension & list comp.
    (2) Set amd dictionary comp.
'''

print("===== What is Comprehension & list comp =====")
# Comprehension acts like spread operator:

''' Comprehension general suntax
    a) *iterable
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>
'''

# list comp.
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("-----")
people = [("JON", 20), ("IKA", 19), ("Odil", 25)]
list_people = [person[0] for person in people]  # b version
print("list_people:", list_people)

print("-----")
cars = [
    ("tiko", 78),
    ("Damas", 87),
    ("nexia", 116),
    ("lada", 109),
    ("epica", 33)
]

list_cars = [car for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)
print("===== Set amd dictionary comp =====")
