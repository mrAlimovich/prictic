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

# we can not mutate Tuple
animals = ("dog", "cat", "fish", "Lion")
tuple_pbj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"

# try avoid this
peaople = "Odil", "Ika"
animals = "dog",


print("==== Unpacking arguments ====")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z)  # list


# *args > tuple
def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)
calculate(0, 2, 300)
calculate(5, 7)

print("-----")
# **kwargs > dictionary


def introduce(**kwargs):
    print(f"the type(**kwarg) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old!")


# CALL
introduce(name="ODIL", age=36)
introduce(name="IKA", age=40, single=True)
print("-----")


def greating(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


# CALL
greating("HI", True, 10, name="Odil", age=22)


print("==== Zip ====")
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
print("zipped:", zipped)
result = list(zipped)
print(f"the result: {result}")
