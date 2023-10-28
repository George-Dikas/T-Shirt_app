import re
import time
from merge_sort_algorithm import merge_sort
from bubble_sort_algorithm import bubble_sort
from bucket_sort_algorithm import bucket_sort

""" CALL OF FUNCTIONS bubble_sort, merge_sort, bucket_sort AND CALCULATION OF EACH FUCTION RUNNING TIME """

#Select the type of sort 
def sort_menu_func(myList):
    
    print("=====================================================================================================")
    values=("1", "2", "3", "4", "5", "6") #Valid values

    input_text = """
                    A)Size in ascending:1  \nB)Size in descending:2 \nC)Color in ascending:3 \nD)Color in descending:4 \nE)Fabric in ascending:5
                    F)Fabric in descending:6 \nPlease choose one type of sort:
                 """

    input_text = re.sub('^[\t ]*', '', input_text.strip(), flags=re.MULTILINE)
    
    while True:
        ch = input(input_text)

        if ch not in values:
            print("\nWrong choice, please try again!")
        else: break

    #Call three particular functions for each sort choice
    #Two different lists to copy f_list. One list for every fuction to compare durations
    #The sort will be presented by one fuction each time
    #Function returns algorithms' durations
    l2 = myList.copy()
    l3 = myList.copy()

    #Size in asceding:ch=1/descending:ch2 - Sorted list by merge_sort
    if ch=="1" or ch=="2":                  

        dt1 = time.time()                   #Time before the call of function                
        merge_sort(myList, 'size', ch)
        for i in range(10000000):pass       #Time delay    
        dt2 = time.time()                   #Time after return of function
        total_time1 = round(dt2 - dt1, 3)   #Total Time

        dt1 = time.time()                
        bubble_sort(l2, 'size', ch)
        for i in range(10000000):pass    
        dt2 = time.time()               
        total_time2 = round(dt2 - dt1, 3)          

        dt1 = time.time()                
        bucket_sort(l3, 'size', ch)
        for i in range(10000000):pass   
        dt2 = time.time()               
        total_time3 = round(dt2 - dt1, 3)                  

    #Color in asceding:ch=1/descending:ch2 - Sorted list by bubble_sort
    elif ch=="3" or ch=="4":

        dt1 = time.time()                               
        merge_sort(l2, 'color', ch)
        for i in range(10000000):pass       
        dt2 = time.time()               
        total_time1 = round(dt2 - dt1, 3)          

        dt1 = time.time()                
        bubble_sort(myList, 'color', ch)
        for i in range(10000000):pass    
        dt2 = time.time()               
        total_time2 = round(dt2 - dt1, 3)        

        dt1 = time.time()                
        bucket_sort(l3, 'color', ch)
        for i in range(10000000):pass    
        dt2 = time.time()               
        total_time3 = round(dt2 - dt1, 3) 
        
    #Fabric in asceding:ch=1/descending:ch2 - Sorted list by bucket_sort
    else:

        dt1 = time.time()                               
        merge_sort(l2, 'fabric', ch)
        for i in range(10000000):pass 
        dt2 = time.time()           
        total_time1 = round(dt2 - dt1, 3)         

        dt1 = time.time()               
        bubble_sort(l3, 'fabric', ch)
        for i in range(10000000):pass    
        dt2 = time.time()               
        total_time2 = round(dt2 - dt1, 3)         

        dt1 = time.time()                
        bucket_sort(myList, 'fabric', ch)
        for i in range(10000000):pass   
        dt2 = time.time()               
        total_time3 = round(dt2 - dt1, 3)
        
    return (total_time1, total_time2, total_time3)    
