import addition
import multiply

def choose():
    choice = input("choose an operation")

    if choice == "add":
        result = addition.add(input("number one"), input("number one"))
    elif choice == "multiply":
        result = multiply.mul(input("number one"), input("number one"))

    return result

while True:
    choose()

