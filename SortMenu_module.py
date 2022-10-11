import time
from MergeSortAlg import *
from BubbleSortAlg import *
from BucketSortAlg import bucketSort

### CALL OF FUNCTIONS bubbleSort, mergeSort, bucketSort AND CALCULATION OF EACH FUCTION RUNNING TIME

#Select the type of sort 
def sort_menu(myList):
    
    print("=====================================================================================================")
    values=("1", "2", "3", "4", "5", "6") #Valid values

    while True:
        ch=input("""A)Size in ascending:1  \nB)Size in descending:2 \nC)Color in ascending:3 \nD)Color in descending:4 \nE)Fabric in ascending:5 
F)Fabric in descending:6 \nPlease choose one type of sort:""")

        if ch not in values:
            print("\nWrong choice, please try again!")
        else: break

    #Call three particular functions for each sort choice

    #Two different lists to copy f_list. One list for every fuction to compare durations
    #The sort will be presented by one fuction each time
    l2 = myList.copy()
    l3 = myList.copy()

    #Size in asceding:ch=1/descending:ch2 - Sorted list by mergeSort
    if (ch=="1" or ch=="2"):                  

        dt1 = time.time()               #Time before the call of function                
        mergeSort(myList,1,ch)
        for i in range(10000000):pass   #Time delay    
        dt2 = time.time()               #Time after return of function
        total_time1 = dt2 - dt1         #Total Time

        dt1 = time.time()                
        bubbleSort(l2,1,ch)
        for i in range(10000000):pass    
        dt2 = time.time()               
        total_time2 = dt2 - dt1         

        dt1 = time.time()                
        bucketSort(l3,1,ch)
        for i in range(10000000):pass   
        dt2 = time.time()               
        total_time3 = dt2 - dt1                 

    #Color in asceding:ch=1/descending:ch2 - Sorted list by bubbleSort
    elif (ch=="3" or ch=="4"):

        dt1 = time.time()                               
        mergeSort(l2,0,ch)
        for i in range(10000000):pass       
        dt2 = time.time()               
        total_time1 = dt2 - dt1         

        dt1 = time.time()                
        bubbleSort(myList,0,ch)
        for i in range(10000000):pass    
        dt2 = time.time()               
        total_time2 = dt2 - dt1         

        dt1 = time.time()                
        bucketSort(l3,0,ch)
        for i in range(10000000):pass    
        dt2 = time.time()               
        total_time3 = dt2 - dt1
        
    #Fabric in asceding:ch=1/descending:ch2 - Sorted list by bucketSort
    else:

        dt1 = time.time()                               
        mergeSort(l2,2,ch)
        for i in range(10000000):pass 
        dt2 = time.time()           
        total_time1 = dt2 - dt1         

        dt1 = time.time()               
        bubbleSort(l3,2,ch)
        for i in range(10000000):pass    
        dt2 = time.time()               
        total_time2 = dt2 - dt1         

        dt1 = time.time()                
        bucketSort(myList,2,ch)
        for i in range(10000000):pass   
        dt2 = time.time()               
        total_time3 = dt2 - dt1
        
    return (total_time1, total_time2, total_time3)    
