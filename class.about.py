''' CLASS
    (1) What is class
    (2) ordirary va static properties
    (3) special methods
'''

print("==== What is class ====")
# class - blueprint for object creation!
# structure > state constructor method


class Person():
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} say i am {self.age}!")

    @classmethod
    def explain(cls):
        print("static method property executed!")


Person1 = Person("Ikromjon", 36)
Person2 = Person("Odil", 35)
Person3 = Person("ALim", 33)

# ordinary state property
print("person1.name:", Person1.name)

# ordinary method
Person1.introduce()
Person2.say_age()


print("==== ordirary va static properties ====")
# sttic state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()


print("==== special/magic methods ====")
# Python's most common spedial method are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"the {self.name} started engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")

    def __str__(self):
        return f"{self.name} was producted in {self.year} year!"

    def __call__(self):
        print("Object called as function")
        return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("-----")
your_car = Car("Tayota", 2026)
print(your_car)
your_car()
response = your_car()  # CALL
print("response:", response)
