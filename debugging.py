''' Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & Extermal Package
    (3) Debugging
'''

from PIL import Image
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
''' Package Managers:pip pipenv npm yarn composer brew '''
# Extermal Package > http://pypi.org/

# with Image.open("material/images.jpg") as img_obj:
#    resize_img = img_obj.resize((200, 200))
#    resize_img.show()
#    resize_img.save("material/sample.jpg")


print("===== Debugging =====")


def get_summary(*args):  # Define
    total_amount = 0
    for a in args:
        total_amount += a
    return total_amount  # solve the bug via debugging


test = 100
result = get_summary(1, 2, 3, 4, 5)  # Call
print("result:", result)
