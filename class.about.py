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
