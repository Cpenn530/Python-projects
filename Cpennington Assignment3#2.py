#Collin Pennington
#2/21/2025
# Chapter 3. A program that calculates the area of two rectangles then telling the users which is bigger.

#input measurments 
len1 = float(input("What is the length of rectangle one?: "))
wid1 = float(input("What is the width of rectangle one?: "))
len2 = float(input("What is the length of rectangle two?: "))
wid2 = float(input("What is the width of rectangle two?: "))
#Calculations
area1 = (len1 * wid1)
area2 = (len2 * wid2)
#Comparrison
if (area1 > area2):
    print ("Rectangle one is greater ")
elif (area1==area2):
    print("Both rectangles are the same")
else:
    print("Rectangle two is greater")
    