''' FUNCTIONS
(1) Define vs CALL
(2) Parametr vs Argument
(3) Keyword & defult arguments
(4) Scope
'''

print("==== DEFINE vs CALL ====")
# built in function > print() type()
# Function - rousable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - build
def great(a):
    print(f"How do you do, {a}")


def greating(b):
    print("greating is executed")
    return f"Hi {b}"


# CALL - execute
result1 = great("Ikromjon")
print("result1:", result1)

result2 = greating("Odil")
print("result2:", result2)
