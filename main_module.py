from menu import intro_menu, color_menu, size_menu, fabric_menu, payment_menu
from sort_menu import sort_menu_func

""" MAIN MODULE """

class TShirt:
    def __init__(self, color, size, fabric, payment_method):
        self.color = color
        self.size = size
        self.fabric = fabric
        self.payment_method = payment_method


def main():
    print("\n\n\t\t\tI========= T-shirt App =========I")
    
    t_shirts_list=[]
    
    while True:
        ch=intro_menu()
    
        if ch=="1":
            t_shirts_list.append(TShirt(color_menu(), size_menu(), fabric_menu(), payment_menu()))            

        else:
            print("\nThank you!\nYou chose to terminate the process.")
            break

    print("\nYour choices and payment methods")
    print("-----------------------------------------------------------------------------------------------------")
    if len(t_shirts_list) == 0:
        print("THERE IS NOT ANY T-SHIRTS INSIDE SHOPPING BASKET")
    
    else:
        for i in range(len(t_shirts_list)):
            print(f"T-shirt {i+1}: ", t_shirts_list[i].color.ljust(18), t_shirts_list[i].size.ljust(18), 
            t_shirts_list[i].fabric.ljust(18),  t_shirts_list[i].payment_method.ljust(18))
 
        if len(t_shirts_list) > 1:
            Durations=() #Tupple for the durations
        
            print("\n\nIt's time to sort your choices!")
            Durations = sort_menu_func(t_shirts_list)

            print("\n")
            print(f"Merge Sort Duration:{Durations[0]} sec")
            print(f"Bubble Sort Duration:{Durations[1]} sec")
            print(f"Bucket Sort Duration:{Durations[2]} sec")

            print("\nShorted list with your T-shirts") 
            print("-----------------------------------------------------------------------------------------------------") 
            for i in range(len(t_shirts_list)):
                print(f"T-shirt {i+1}: ", t_shirts_list[i].color.ljust(18), t_shirts_list[i].size.ljust(18), 
                t_shirts_list[i].fabric.ljust(18),  t_shirts_list[i].payment_method.ljust(18))

            
if __name__=="__main__":
    main()
