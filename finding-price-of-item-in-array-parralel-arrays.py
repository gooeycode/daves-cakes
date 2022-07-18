#click execute to use this program

import time

#declerations
MSG_YES = "This cake item is in the database, getting the price for you..."
MSG_NO = "This cake item is not in the database."
itemNoList = [234, 813, 629, 887, 1423, 35]
itemPrices = [3.00, 14.34, 2.20, 34.8, 28.9, 7.34]
foundIt = ""
SIZE = 6
QUIT = int(999)
#functions
def findItems():
    global itemInput
    foundIt = "N"
    x = 0
    #while loop control variable hasnt passed array size AND an item hasnt been found
    while (x < SIZE) and (foundIt == "N"):
        if int(itemInput) == int(itemNoList[x]):
            foundIt = "Y"
            price = itemPrices[x]
        x = x + 1
    #if the item has been found    
    if foundIt == "Y":
        print(MSG_YES)
        time.sleep(2)
        print("Cake item number is", itemInput)
        time.sleep(2)
        print("Cake item price is £", price)
        time.sleep(2)
    #else if it hasnt been found
    else:
        print(MSG_NO)
        time.sleep(1)
    #reprompt and enter new item number
    print("enter your cake item number and the price will be returned, or 999 to quit program")
    itemInput = int(input())
    time.sleep(1)
#program start
print("Hello, welcome to Daves cakes")
time.sleep(2)
print("this program will find your cake price")
time.sleep(2)
print("enter your cake item number and the price will be returned, or 999 to quit program")
time.sleep(2)
#enter item number
itemInput = int(input())
#while item does not equal quit
while itemInput != QUIT:
    #find item
    findItems()
#end of program