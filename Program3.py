#Create a program that which you will enter the amount of money you have, 
# it will also ask for the price of an apple.
#display tha maximum number of apples that you can buy and the remaining money that you will have
#You can buy  ______ apples and your change is ______ pesos.

def get_yourMoney():
    _yourMoney = int(input("Enter the amount of money you have: "))
    return _yourMoney

def get_applePrice():
    _applePrice = int(input("How much for an apple?: "))
    return _applePrice
    
def get_maxApples():
    _maxApples = yourMoney // applePrice
    return _maxApples

def get_yourChange():
    _yourChange = yourMoney - maxApples * applePrice
    return _yourChange

def display(maxApplesX, yourChangeX):
    print(f"You can buy {maxApples} apples and your change is {yourChange} pesos.")
#Steps
#1. ask for the amount of money
yourMoney = get_yourMoney()
#2. ask for the price of an apple
applePrice = get_applePrice() 
#3. compute the maximum amount of apples available for purchase
maxApples = get_maxApples()
#4. compute the change of the given amount of money
yourChange = get_yourChange()
#5. display
display(maxApples, yourChange)