''' FUNCTIONS
(1) Define vs CALL
(2) Parametr vs Argument
(3) Keyword & defult arguments
(4) Scope
'''

print("==== DEFINE (parameter) vs CALL (argument) ====")
# built in function > print() type()
# Function - rousable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - parameter
def great(a):
    print(f"How do you do, {a}")


def greating(b):
    print("greating is executed")
    return f"Hi {b}"


# CALL - argument
result1 = great("Ikromjon")
print("result1:", result1)

result2 = greating("Odil")
print("result2:", result2)


print("==== Keyword & defult arguments ====")


# DEFINE
def give_great(name, age=22):
    print("give_great is executed")
    return f"HI {name}, you are {age} years old"


# CALL
result3 = give_great(name="Odil", age=28)
print("result3:", result3)

result4 = give_great("Odiljon")
print("result4:", result4)


print("==== SCOPE ====")
b = 100  # 3


# DEFINE
def calculate(a):  # 2
    c = a * b  # 1
    print(f"the c value: {c}")


# CALL
calculate(5)
