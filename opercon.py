''' OPERATION & CONDITIONS
    (1) Operators
    (2) Condition
    (3) Logical Operators
'''

print("==== Operators ====")
# + - > >= < <= * /  is ==  //  % +=  **

a = 19
b = 5

print(a / b)
result = a // b
left = a % b
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)

print("b**2:", b**2)
print("b**3:", b**3)

print("="*5)

c = dict(name="Odil", age=36)
d = dict(name="Odil", age=36)
e = c
print("c==d", c == d)  # only value
print(id(c), id(d), id(e))

data = c is d
print("c is d", c is d)
print("c is d", c is e)
