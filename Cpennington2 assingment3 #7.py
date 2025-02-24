#Collin Pennington
#2/21/2025
#This program calculates how many packs of hotdogs you would need for a cookout with minimal buns left over

#Constants
DOGS = 10
BUNS = 8

#inputs
people = int(input("How many people are coming to the cookout?: "))
dogPerPerson = int(input("How many hot dogs will each person eat?: "))

#Calculations
totalDogs = (people*dogPerPerson)
totalDPacks = (totalDogs // DOGS)
totalBunPack = (totalDogs // BUNS)


#if statements for MOD
if ((totalDogs % DOGS) > 0):
    totalDPacks +=1

    
if ((totalDogs % BUNS) > 0):
    totalBunPack += 1
    
#left overs
xDog= (totalDPacks*DOGS) - totalDogs
xBuns= (totalBunPack*BUNS) - totalDogs

print(f"Total Hot dog packs needed:{totalDPacks}")
print(f"Total Hot bun packs needed:{totalBunPack}")
print(f"Total left over hot dogs:{xDog}")
print(f"Total left over buns:{xBuns}")
