from strategy_pattern import CreditDebitCard, MoneyBank, Cash, Context

""" FUNCTIONS FOR ADDING T-SHIRT, COLOR, SIZE, FABRIC AND PAYMENT METHOD USER'S CHOICE """

#Buy or Die Choice
def intro_menu():
    values=("1", "2") #Valid values

    while True:
        ch=input("\n\nPress '1' to add a T-Shirt to shopping basket or press '2' to terminate the process:")

        if ch not in values:
            print("Wrong choice, please try again!")
        else: break

    return ch


#Select Color
def color_menu():
    print("=====================================================================================================")
    values=("RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "VIOLET") 

    while True:
        ch=input("A)RED \nB)ORANGE \nC)YELLOW \nD)GREEN \nE)BLUE \nF)INDIGO \nG)VIOLET \nPlease type the color:") 

        if ch not in values:
            print("\nWrong choice, please try again!") 
        else: break

    return ch


#Select Size
def size_menu():
    print("=====================================================================================================")
    values=("XS", "S", "M", "L", "XL", "XXL", "XXXL")

    while True:
        ch=input("A)XS \nB)S \nC)M \nD)L \nE)XL \nF)XXL \nG)XXXL \nPlease type the size:") 

        if ch not in values:
            print("\nWrong choice, please try again!") 
        else: break

    return ch


#Select fabric
def fabric_menu():
    print("=====================================================================================================")
    values=("WOOL", "COTTON", "POLYESTER", "RAYON", "LINEN", "CASHMERE", "SILK") 

    while True:
        ch=input("A)WOOL \nB)COTTON \nC)POLYESTER \nD)RAYON \nE)LINEN \nF)CASHMERE \nG)SILK \nPlease type the fabric:") 

        if ch not in values:
            print("\nWrong choice, please try again!") 
        else: break

    return ch


#Select payment method
def payment_menu():
    print("=====================================================================================================")
    values=("1", "2", "3") 

    while True:
        ch=input("A)Credit/Debit cards 1 \nB)Money/Bank Transfer 2 \nC)Cash 3 \nPlease press '1', '2' or '3':") 

        if ch not in values:
            print("\nWrong choice, please try again!") 
        else: break

    print("=====================================================================================================")

    #Return an object after the payment choice
    if ch=="1":
        context = Context(CreditDebitCard())
        return str(context.execute_strategy())

    elif ch=="2":
         context = Context(MoneyBank())
         return str(context.execute_strategy())

    else:
        context = Context(Cash())
        return str(context.execute_strategy())
