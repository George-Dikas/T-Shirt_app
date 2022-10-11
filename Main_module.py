from Menu_module import *  
from SortMenu_module import sort_menu

### MAIN PROGRAM

def main():

    list1=[]
    f_list=[]
   
    print("\n\n\t\t\tI========= T-shirt App =========I")
    
    while True:

        ch=intro_menu()
        if ch=="1":
            color=color_menu()   
            size=size_menu()     
            fabric=fabric_menu() 
            pay=payment_menu()   

            list1.append(color)  
            list1.append(size)   
            list1.append(fabric) 
            list1.append(pay)    

            f_list.append(list1) 
            list1=[]             

        else:
            print("\nThank you!\nYou chose to terminate the process.")
            break

    print("\nYour choices and payment methods")
    print("-----------------------------------------------------------------------------------------------------")
    if len(f_list) == 0:
        print("THERE IS NOT ANY T-SHIRTS INSIDE SHOPPING BASKET")

    else:
        for i in range(len(f_list)):
            print("T-shirt {}: ".format(i+1), end="")
            for j in range(4):
                print(f_list[i][j].ljust(18), end="")
            print()
 
        Durations=() #Tupple for the durations
    
        print("\n\nIt's time to sort your choices!")
        Durations = sort_menu(f_list)

        print("\n")
        print("Merge Sort Duration:{}sec".format(Durations[0]))
        print("Bubble Sort Duration:{}sec".format(Durations[1]))
        print("Bucket Sort Duration:{}sec".format(Durations[2]))

        print("\nShorted list with your T-shirts") 
        print("-----------------------------------------------------------------------------------------------------") 
        for i in range(len(f_list)):
            print("T-shirt {}: ".format(i+1),end="")
            for j in range(3):
                print(f_list[i][j].ljust(18), end="")
            print()

            
if __name__=="__main__":
    main()
