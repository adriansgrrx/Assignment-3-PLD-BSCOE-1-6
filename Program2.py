#Create a program that will ask how many apples and oranges you want to buy
#applePrice = (20)
#orangePrice = (25)
#The total amount is

def get_apple():
    _apple = int(input("How many apples do you want to buy?: "))
    return _apple

def get_orange():
    _orange = int(input("How many oranges do you want to buy?: "))
    return _orange

def get_applePrice():
    _applePrice = 25
    return _applePrice

def get_orangePrice():
    _orangePrice = 20
    return _orangePrice

def get_totalApples():
    _totalApples = appleQuestion * applePrice
    return _totalApples

def get_totalOranges():
    _totalOranges = orangeQuestion * orangePrice
    return _totalOranges

def get_total():
    _sum = totalApples + totalOranges
    return _sum

def display(total):
    print(f"The total amount is {total}.")
#Steps
#1. ask for the number of appples to be purchase
appleQuestion = get_apple()
#2. ask for the number of oranges to be purchase
orangeQuestion = get_orange()
#3. define the price of an apple
applePrice = get_applePrice()
#4. define the price of an orange
orangePrice = get_orangePrice()
#5. compute for the total price of the apples
totalApples = get_totalApples()
#6. compute for the total price of the oranges
totalOranges = get_totalOranges()
#7. compute for the total amount of apples and oranges
total = get_total()
#8. display
display(total)