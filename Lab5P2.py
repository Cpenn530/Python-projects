#Collin Pennington
#3/28/25
#Deck building estimate
#Constant
PI=3.14
COST_PER_SQFT = 7.45
TAX_RATE = 0.06
#Func that welcomes
def welcome():
    print(f"Welcome to Collin Marvelous Decks\nOwned and Operated by Collin Pennington")
#Func to get info
def getInfo():
    name = input("Enter your full name: ")
    cell = input("Enter your cellphone: ")
    email = input("enter your full email address: ")
    return name, cell, email
#Func select shape
def selectShape():
    choice= 0
    while choice != 1 and choice != 2 and choice != 3:
        print(f"Different decks we build")
        print(f"1. Rectagular")
        print(f"2. Circular")
        print(f"3. Trapezoidal")
        
        uinput=input("Please enter the corresponding number to the shape of deck you would like: ")
        
        if uinput == "1" or uinput == "2" or uinput == "3":
            choice = int(uinput)
        else:
            print("This is invalid. Must enter either 1, 2, or 3")
    return choice
#input Validation
def valInput(str):
    val = float(input(str))
    while val <=0:
        print("ERROR-Input is invalid. Must be greater than 0")
        val=float(input(str))
    return val
# Recatangle dimension
def getRecDim():
   length = valInput("Enter the length of the deck in feet please: ")
   width = valInput("Enter the width of the deck in feet please: ")
   return length, width
#Rectangle calc
def calcRecArea(length,width):
    area = length * width
    return area
#Circle radius
def getCirDim():
    diameter = valInput("Enter the diameter of the deck in feet please: ")
    radius = diameter / 2
    return radius
#Area of cricle 
def calcCirArea(radius):
    area = PI * radius * radius
    return area
#get trapizoid dimensions
def getTrapDim():
    sLen = valInput("Enter the shorter sides length of the trapezoids length in feet: ")
    lLen = valInput("Enter the lonnger sides length of the trapezoids length in feet: ")
    height = valInput("Enter the height of the trapezoid in feet: ")
    return sLen, lLen, height
#Trap calc
def calcTrapArea(sLen,lLen,height):
    area = (sLen + lLen) /2 * height
    return area
#Calc total price
def calcTotalPrice(area):
    cost = area * COST_PER_SQFT
    return cost
#Displays estimate
def displayEstimate(name,cell,email,area,price):
    tax = price * TAX_RATE
    finalP = price + tax
    print(f"\nName: {name:>31}")
    print(f"Phone: {cell:>30}")
    print(f"Email: {email:>30}")
    print(f"\nTotal area: {area:.2f} square feet")
    print(f"The cost per square foot is ${COST_PER_SQFT}")
    print(f"\nTotal Cost before tax: ${price:.2f}")
    print(f"Sales Tax: ${tax:.2f}")
    print(f"Final Cost: ${finalP:.2f}")
    print(f"This estimate is valid for 60 days.")
#The good bye function ending the estimate
def goodBye():
    print("Thank you for using Collin's MArvelous Decks!\nHave a good day!")
    
    
    
        
    
#Main
def main():
    welcome()
    name, cell, email = getInfo()
    again = "y"
    while again == "y" or again == "Y":
        choice = selectShape()
        if choice == 1:
            length, width = getRecDim()
            area = calcRecArea(length, width)
        elif choice == 2:
            radius = getCirDim()
            area = calcCirArea(radius)
        else:
            sLen, lLen, height = getTrapDim()
            area = calcTrapArea(sLen,lLen, height)
        price = calcTotalPrice(area)
        displayEstimate(name, cell, email, area, price)
        again = input("\nWould you like another estimate? (Y/N): ")
        if again == "n" or again == "N":
            goodBye()
    
    

main()