""" BUBBLE SORT ALGORITHM """

def bubble_sort(myList, attr_as_str, ch):    #attr_as_str: Attribute of object as string, ch: Choice of type ascending/descending 
                                                                
    n = len(myList)
  
    #Traverse through all list elements
    for i in range(n-1):
        swapped = False
  
        #Last i elements are already in place
        for j in range(0, n-i-1):

            #Traverse the array from 0 to n-i-1
            #Swap if the element found is greater than the next element
            if ch=="1" or ch=="3" or ch=="5":                                       #ASC

                if getattr(myList[j], attr_as_str) > getattr(myList[j+1], attr_as_str):
                    myList[j], myList[j+1] = myList[j+1], myList[j]
                    swapped = True
                
                #Check for second or third sort level
                elif getattr(myList[j], attr_as_str) == getattr(myList[j+1], attr_as_str):

                    if attr_as_str == 'color':                                      #Color/Size            
                        if myList[j].size > myList[j+1].size:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j].size == myList[j+1].size:                    #Color/Size/Fabric
                            if myList[j].fabric > myList[j+1].fabric:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True

                    elif attr_as_str == 'size':                                     #Size/Fabric    
                        if myList[j].fabric > myList[j+1].fabric:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j].fabric == myList[j+1].fabric:                #Size/Fabric/Color
                            if myList[j].color > myList[j+1].color:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True

                    else:                                                           #Fabric/Color
                        if myList[j].color > myList[j+1].color:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j].color == myList[j+1].color:                  #Fabric/Color/Size
                            if myList[j].size > myList[j+1].size:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True

            else:                                                                   #DESC

                if getattr(myList[j], attr_as_str) < getattr(myList[j+1], attr_as_str):
                    myList[j], myList[j+1] = myList[j+1], myList[j]
                    swapped = True

                elif getattr(myList[j], attr_as_str) == getattr(myList[j+1], attr_as_str):

                    if attr_as_str == 'color':                                      #Color/Size            
                        if myList[j].size < myList[j+1].size:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j].size == myList[j+1].size:                    #Color/Size/Fabric
                            if myList[j].fabric < myList[j+1].fabric:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True

                    elif attr_as_str == 'size':                                     #Size/Fabric    
                        if myList[j].fabric < myList[j+1].fabric:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j].fabric == myList[j+1].fabric:                #Size/Fabric/Color
                            if myList[j].color < myList[j+1].color:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True

                    else:                                                           #Fabric/Color
                        if myList[j].color < myList[j+1].color:
                            myList[j], myList[j+1] = myList[j+1], myList[j]
                            swapped = True

                        elif myList[j].color == myList[j+1].color:                  #Fabric/Color/Size
                            if myList[j].size < myList[j+1].size:
                                myList[j], myList[j+1] = myList[j+1], myList[j]
                                swapped = True
        
        #If no two elements were swapped by inner loop, then break
        if swapped == False:
            break
