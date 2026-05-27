''' CLASS deep diving
    (1) ENCAPSOLATION
    (2) INHERITENCE <
    (3) POLIMORPHISM <
'''

print("==== INHERITENCE ====")
# PAREN > CHILD
# Parent only provides public & protected properties(state + method) to children!


class Animal:
    decription = "The class parent for animals"

    def __init__(self, voice):
        self._status = "animal is aliive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice : {self.voice}")


class Dog(Animal):  # Child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


class Cat(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("REX", "wow", True)
cat = Cat("TOM", "myeow", True)
fish = Fish("Nemo", "ZzZ", "False")

dog.introduce()
cat.introduce()
fish.introduce()

print("------")
dog.make_voice()
fish.make_voice()

print("------")
print(Animal.decription)
print(dog.decription)

print(dog.voice, fish.voice)
print("dog.status:", dog._status)
print("cat.status:", cat._status)
