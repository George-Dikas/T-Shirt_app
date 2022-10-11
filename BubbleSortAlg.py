### BUBBLESORT ALGORITHM

def bubbleSort(myList,p,ch):    #p:Position of inner list, ch:Choice of type ascending/descending

    n = len(myList)
  
    #Traverse through all list elements
    for i in range(n-1):
        swapped = False
  
        #Last i elements are already in place
        for j in range(0, n-i-1):

            #Traverse the array from 0 to n-i-1
            #Swap if the element found is greater than the next element
            if (ch=="1" or ch=="3" or ch=="5"): #ASC

                if myList[j][p] > myList[j+1][p]:
                    myList[j], myList[j+1] = myList[j+1], myList[j]
                    swapped = True
                
                #Check for second or third sort level
                elif myList[j][p] == myList[j+1][p]:

                    if(p==0):                                   #Color/Size            
                        if myList[j][1] > myList[j+1][1]:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j][1] == myList[j+1][1]:    #Color/Size/Fabric
                            if myList[j][2] > myList[j+1][2]:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True

                    elif(p==1):                                 #Size/Fabric    
                        if myList[j][2] > myList[j+1][2]:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j][2] == myList[j+1][2]:    #Size/Fabric/Color
                            if myList[j][0] > myList[j+1][0]:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True

                    else:                                       #Fabric/Color
                        if myList[j][0] > myList[j+1][0]:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j][0] == myList[j+1][0]:    #Fabric/Color/Size
                            if myList[j][1] > myList[j+1][1]:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True

            else: #DESC
                
                if myList[j][p] < myList[j+1][p]:
                    myList[j], myList[j+1] = myList[j+1], myList[j]
                    swapped = True

                elif myList[j][p] == myList[j+1][p]:

                    if(p==0):                                   #Color/Size            
                        if myList[j][1] < myList[j+1][1]:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j][1] == myList[j+1][1]:    #Color/Size/Fabric
                            if myList[j][2] < myList[j+1][2]:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True

                    elif(p==1):                                 #Size/Fabric    
                        if myList[j][2] < myList[j+1][2]:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j][2] == myList[j+1][2]:    #Size/Fabric/Color
                            if myList[j][0] < myList[j+1][0]:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True

                    else:                                       #Fabric/Color
                        if myList[j][0] < myList[j+1][0]:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j][0] == myList[j+1][0]:    #Fabric/Color/Size
                            if myList[j][1] < myList[j+1][1]:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True
        
        #If no two elements were swapped by inner loop, then break
        if swapped == False:
            break
