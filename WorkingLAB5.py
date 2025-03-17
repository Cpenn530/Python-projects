#Collin Pennington
#2/14/2025
#A program for managing sales transactions

#Constants
BACKPACKS = 49.95
PENS = 0.78
PINK = 41.95
PAPER = 25.00
STAX = 0.06
DBACKPACK = 44.96
LDPENS = 0.68
HDPENS = 0.58
REAM = 6.00
DISC_BACK = 3
DiscA = 499.99
DISC =.05
#Customer Management func
def customer_man():
    first = input("Please input your first name:")
    last = input("Please input your last name:")
    po = int(input("Please input your purchase order number:"))
    while po <= 0:
        print("Error- Must enter a number greater than zero")
        po = int(input("Please input your purchase order number:"))
    return last,first,po
#Customer Pur func
def Customer_pur(item):
    quantity = int(input(f"Number of {item} bought: "))
    while quantity < 0:
        print(f"ERROR: Must be a number either 0 or greater!")
        quantity = int(input(f"Number of {item} bought: "))
    return quantity
#Ream of case?
def R_C():
        case = 0
        ream = 0
        p_r = str(input("Would you like a case or ream of paper? (case/ream/none): "))
        while p_r != "case" and p_r != "ream" and p_r!="none":
            print (f"This is invalid must input case, ream , or none")
            p_r = str(input("Would you like a case or ream of paper? (case/ream/none): "))
        if (p_r == "case"):
            case = Customer_pur("cases of paper")
        elif (p_r =="ream"):
            ream = Customer_pur("ream of paper")
        return case,ream,p_r
#sub total func
def Calc_Sub_Total(bpCost,penC,pinkC,paperC,reamC):
    total = bpCost + penC + pinkC+paperC+reamC
    return total
#total calc 
def calc_t(total,salesTax):
    owed = total + Tax
    return owed
#calc ream and case
def calc_c_r(quantity, price):
    return quantity * price

      #Looping the program
def main():
    process = "y"
    while process == 'y' or process =='Y':
        Subtotal = 0
        TOTALI=0
        paperC=0
        reamC=0
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
        print(f"${PAPER} per case / ${REAM} per ream.\n")
        #Call customer info
        last, first, po = customer_man()
        #Print customer info    
        title =("PURCHASE ORDER INVOICE") 
        print(f"Customer: {last}, {first}")
        print(f"PO: {po}")
        #Customer Purchase
        #Backpacks
        bp = Customer_pur("backpacks")
        TOTALI+=bp
        #if statements backpack calcs
        if (bp >= DISC_BACK):
            bpCost = (bp * DBACKPACK)
        else:
            bpCost = bp * BACKPACKS
        Subtotal += bpCost
        print(f"Current Subtotal:${Subtotal:.2f}")
        #Pen
        pen = Customer_pur("pen")
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
    #ink
        pink = Customer_pur("printer ink")
        TOTALI+=pink
        pinkC = pink * PINK
        Subtotal+=pinkC
        print(f"Current Subtotal:${Subtotal:.2f}")
        #case or ream
        case,ream,p_r = R_C()
        
        TOTALI+=case
        TOTALI+=ream
        
        
        if p_r=="case":
            paperC = calc_c_r(case,PAPER)
            Subtotal+=paperC
            print(f"Current Subtotal:${Subtotal:.2f}")
        if p_r=="ream":
            reamC = calc_c_r(ream,REAM)
            Subtotal+=reamC
            print(f"Current Subtotal:${Subtotal:.2f}")

        #Title and name and PO
        print(f"{title:^100}")
        print(f"Customer: {last} {first}")
        print(f"PO: {po}")
    


        #Output of calcs
        if (bp > 0):

            print(f"({bp})Backpack price: ${bpCost:.2f}")
        if (pen > 0):
            print(f"({pen})Pens price: ${penC:.2f}")
        if (pink > 0):
            print(f"({pink})Printer Ink price: ${pinkC:.2f}")
        if (case >0):
            print(f"({case})Printer Paper price: ${paperC:.2f}")
        if (ream >0):
            print(f"({ream})Printer Ream price: ${reamC:.2f}")
        #Subtotal
        Subtotal = Calc_Sub_Total(bpCost,penC,pinkC,paperC,reamC)
        print(f"Sub Price: ${Subtotal:.2f}")

        #Total

        if Subtotal >= DiscA:
            Dis = Subtotal * DISC
            Subtotal -= Dis
            print(f"5% discount applied {Dis:.2f}")
        #sales tax
        salesTax = Subtotal * STAX
    
        Total = Subtotal + salesTax
        print(f"Salex tax: ${salesTax:.2f}")
        print(f"Total Price: ${Total:.2f}")
        print(f"Total Items: {TOTALI}")
        process= str(input("Would you like to do another invoice? (y/n): "))
        while process != "y" and process != 'Y' and process != "n" and process != 'N':
            print(f"This is invalid input either y or n")
            process= str(input("Would you like to do another invoice? (y/n): "))
        
    print(f"Thank you for using me")
main()