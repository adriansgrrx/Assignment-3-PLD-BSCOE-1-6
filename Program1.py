#Create a program that will ask for name, age and address
#Hi, my name is ___ . I am ___ years old and I live in _____ .

def getName():
    _name = input("Enter your name: ")
    return _name

def getAge():
    _age = input("Enter your age: ")
    return _age

def getAddress():
    _address = input("Enter your address: ")
    return _address

def display(nameX, ageX ,addressX):
    print(f"Hi, my name is {name}. I am {age} years old and I live in {address}.")
#Steps
#1. Ask for name
name = getName()
#2. Ask for age
age = getAge()
#3. Ask for address
address = getAddress()
#4. display
display(name, age, address)