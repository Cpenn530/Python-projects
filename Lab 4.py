#Collin Pennington
#2/14/2025
#A program for managing sales transactions

#Constants
BACKPACKS = 49.95
PENS = 0.78
PINK = 41.95
PAPER = 6.00
STAX = 0.06
DBACKPACK = 44.96
LDPENS = 0.68
HDPENS = 0.58
REAM = 25.00
DISC_BACK = 3
DiscA = 499.99
DISC =.05
process = "y"
while process != "n":
    Subtotal = 0
    case = 0
    ream = 0
    TOTALI=0
    reamC=0
    caseC=0
    #Available items
    print("Backpacks:")
    print(f"${BACKPACKS} for each. [10% discount for 3 or more]\n")
    print("Printer Ink:")
    print(f"${PINK} each\n")
    print("Pens:")
    print(f"${PENS} each for 5 or fewer.")
    print(f"${LDPENS} each for 6 to 10 pens.")
    print(f"${HDPENS} each for 11 or more.\n")
    print("Printer Paper:")
    print(f"${PAPER} per ream / ${REAM} per ream.\n")

    #Customer Management
    first = input("Please input your first name:")
    last = input("Please input your last name:")
    title =("PURCHASE ORDER INVOICE")
    po = int(input("Please input your purchase order number:"))
    while po < 0:
        print("Error- Must enter a number greater than zero")
        po = int(input("Please input your purchase order number:"))

    #Customer Purchase
        
    #Backpacks
    bp = int(input("Please input the amount of backpacks bought:"))
    while bp < 0:
        print ("Error- Please input a number starting at 0 or greater")
        bp = int(input("Please input the amount of backpacks bought:"))
    TOTALI+=bp
    
    #if statements backpack calcs
    if (bp >= DISC_BACK):
        bpCost = (bp * DBACKPACK)
    else:
        bpCost = bp * BACKPACKS
    Subtotal += bpCost
    print(f"Current Subtotal:${Subtotal:.2f}")
    
    #Pen
    pen = int(input("Please input the amount of pens bought:"))
    while pen < 0:
        print ("Error- Please input a number starting at 0 or greater")
        pen = int(input("Please input the amount of pens bought:"))
    TOTALI+=pen
    #if pen calcs 
    if (pen >=11):
        penC=pen*HDPENS
    elif(pen >= 6 and pen <= 10):
        penC = pen * LDPENS
    else:
        penC = pen * PENS
    Subtotal+=penC
    print(f"Current Subtotal:${Subtotal:.2f}")
    
    
    pink = int(input("Please input the amount of printer ink bought:"))
    while pink < 0:
        print ("Error- Please input a number starting at 0 or greater")
        pink = int(input("Please input the amount of printer ink bought:"))
    TOTALI+=pink
    pinkC = pink * PINK
    Subtotal+=pinkC
    print(f"Current Subtotal:${Subtotal:.2f}")
    
    
    p_r = str(input("Would you like a case or ream of paper? (case/ream): "))
    if (p_r == "case"):
        case = int(input("Please input the amount of printer paper bought:"))
    elif (p_r =="ream"):
        ream = int(input("Please input the amount of reams of paper bought:"))
    TOTALI+=ream
    TOTALI+=case
    if p_r=="case":
        paperC = case * PAPER
        Subtotal+=paperC
        print(f"Current Subtotal:${Subtotal:.2f}")
    if p_r=="ream":
        reamC = ream * REAM
        Subtotal+=reamC
        print(f"Current Subtotal:${Subtotal:.2f}")
#if statements for printing only products bought 
    if (bp >0):
        print(f"Amount of backpacks: {bp}")
    if (pen > 0):
        print(f"Amount of pens: {pen}")
    if (pink > 0):
        print(f"Amount of printer ink: {pink}")
    if (p_r =="case" and case>0):
        print(f"Amount of printer paper: {case}")
    if (p_r == "ream" and ream >0):
        print (f"Amount of reams bought: {ream}")
    #Title and name and PO
    print(f"{title:^100}")
    print(f"Customer: {last} {first}")
    print(f"PO: {po}")
    
 

    
    
   


    #Output of calcs
    if (bp > 0):
        print(f"Backpack price: ${bpCost:.2f}")
    if (pen > 0):
        print(f"Pens price: ${penC:.2f}")
    if (pink > 0):
        print(f"Printer Ink price: ${pinkC:.2f}")
    if (case >0):
        print(f"Printer Paper price: ${paperC:.2f}")
    if (ream >0):
        print(f"Printer Ream price: ${reamC:.2f}")
    #Subtotal
    Subtotal = bpCost + penC + pinkC + paperC + reamC
    print(f"Subtotal price: ${Subtotal:.2f}")
    #Total
    
    
    if Subtotal >= DiscA:
        Dis = Subtotal * DISC
        Subtotal -= Dis
        print(f"5% discount applied")
    #sales tax
    salesTax = Subtotal * STAX
    
    Total = Subtotal + salesTax
    
    print(f"Total Price: ${Total:.2f}")
    print(f"Total Items: {TOTALI}")
    
    process= str(input("Would you like to do another invoice? (y/n): "))
print(f"Thank you for using me")