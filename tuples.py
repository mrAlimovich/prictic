''' Tuple
(1) What is tuple : tuble vs list
(2) Unpacking arguments
(3) Zip
'''

print("==== What is tuple : tuble vs list ====")
# Java/PHP/NoteJS array => Python list, array

# Literal
numbs = [3, 5, 1, 2]

# Canstructor
letters = list("Hello World!")

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

# Tuple
animals = ("dog", "cat", "fish", "Lion")
tuple_pbj = ("MIT", 100, True, None)

print(animals[0])
animals[0] = "bird"


print("==== Unpacking arguments ====")
print("==== Zip ====")
