''' Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & Extermal Package
    (3) Debugging
'''

import turtle
print("===== Python Packages & Core Package =====")
''' Python Packages/Modules: Core, File and Extermal '''
# Core Packages > https://docs.python.org/3/library/


# Core Package
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(160)
# turtle.done()

print("----")
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with - Context manager
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("DONE")


print("===== Package Manager & Extermal Package =====")
print("===== Debugging =====")
