def shoplist():
    quitshop = False
    shoppinglist = []

    while (quitshop == False):
        print(" ")
        print("Your shopping list contains ")
        print(" ")
        for item in shoppinglist:
            print(item)

        print(" ")
        print("Menu")
        print(" ")
        print("0 = add multiple items to list")
        print("1 = add item to list")
        print("2 = remove item from end")
        print("3 = remove specific item")
        print("4 = reverse list")
        print("5 = print out some of the list")
        print("6 = sort into alphabetical order")
        print("9 = quit")
        userchoice = int(input("Please enter the option you want to proceed with "))

        if (userchoice == 0):
            print("You chose option 0")

            additem = ""

            while additem != "stop":
                additem = input("Please enter item for list: ")

                if additem != "stop" and additem:
                    shoppinglist.append(additem)

        elif (userchoice == 1):

            print("You chose option 1")
            additem = input("Please enter an item you want to add: ")
            shoppinglist.append(additem)
        elif (userchoice == 2):
            print("You chose option 2")
            print("The program will remove the last item from the list")
            shoppinglist.pop()
        elif (userchoice == 3):
            print("You chose option 3")
            positiontode1 = int(input("Which item would you like to delete? (enter a number)"))
            del (shoppinglist[positiontode1])
        elif (userchoice == 4):
            print("You chose option 4")
            print("This will reverse your list")
            shoppinglist.reverse()
        elif (userchoice == 5):
            print("You chose option 5")
            end = int(input("Which item should we end at? (Insert a number)"))
            for printlist in range(end):
                print(shoppinglist[printlist])
        elif (userchoice == 6):
            print("You chose option 6")
            shoppinglist.sort()
        elif (userchoice == 9):
            print("You have chosen to quit the program")
            quit
            quitshop = True

        else:
            print("error")
            print("Try again")


if __name__ == "__main__":
    shoplist()
