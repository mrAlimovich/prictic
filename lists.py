''' LIST
(1) Working with list
(2) List methods
(3) Lambda Function
(4) enumerate, map, and filter
'''

print("===== Working with list =====")
# Java/PHP/NoteJS array => Python list, array

# Literal
person = {"name": "Odil", "age": 25}  # dictionary
peaple = ("Ika", "ALI", "Lola")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # List
for team in groups:
    print(f"the team: {team}")


# constructor
letters = list("HELLO WORLD!")
print(f"the letters: {letters} and size: {len(letters)}")


print("-----")
fruits = ["apple", "orenge", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0: 2]  # [0,2]
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("===== List methods =====")
# methods > append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the append result: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert result: {letters}")


size = len(letters) - 1
reselt1 = letters.pop(size)  # pop behind
print(f"the pop result1: {reselt1} and letters: {letters}")


reselt2 = letters.pop(0)  # pop front
print(f"the pop result2: {reselt2} and letters: {letters}")


print("-----")
animals = ["dog", "cat", "capynara", "fish", "lion"]
print("animaals:", animals)

animals.remove("lion")
print("remove:", animals)

del animals[2: 4]
print("delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")

print("-----")
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("sort default:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# imutable > sorted function & index() method
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")


print("===== Lambda Function =====")
# lambda is small anonymous function:
def calculate(x, y): return x * y


reselt = calculate(3, 5)
print("result:", reselt)

peaple = [
    ("Ika", 20),
    ("Odi", 19),
    ("Ali", 25),
    ("Bek", 30),
    ("Xon", 40)
]
peaple.sort()
print("people(1)", peaple)

# sort by age via lambda
peaple.sort(key=lambda person: person[1])
print("people(2)", peaple)

print("===== enumerate, map, and filter =====")
# enumerate for index & value

animals = ["dog", "cat", "fish"]  # list
for element in enumerate(animals):
    print("element:", element)

for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")

print("-----")
# similar in dictionary
car_obj = dict(brand="Ferrari", year=2025)  # dict
reselt = car_obj.items()
for (key, value) in reselt:
    print(f"the key: {key} and value {value}")

print("-----")
# map
cars = [
    ("tiko", 78),
    ("Damas", 87),
    ("nexia", 116),
    ("lada", 109),
    ("epica", 33)
]

result_map = map(lambda car: car[0], cars)
print(f"the result_map: {result_map} and type: {type(result_map)}")
new_cars = list(result_map)
print("new_cars", new_cars)

print("-----")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter: {result_filter} and type: {type(result_filter)}")
print(list(result_filter))
