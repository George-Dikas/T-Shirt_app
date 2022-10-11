### MERGESORT ALGORITHM

def mergeSort(myList,p,ch):         #p:Position of inner list, ch:Choice of type ascending/descending     
    
    if len(myList) > 1:             #If list has more than one element
        mid = len(myList) // 2      #finding the mid of the list
        left = myList[:mid]         #Left half of the list
        right = myList[mid:]        #Right half of the list

        mergeSort(left,p,ch)        #Sorting the first half
        mergeSort(right,p,ch)       #Sorting thr second half

        i = j = 0                   #Two iterators for traversing the two halves
        k = 0                       #Iterator for the main list
        
        while i < len(left) and j < len(right):

            if ch=="1" or ch=="3" or ch=="5":   #ASC  

                if left[i][p] < right[j][p]:
                    myList[k] = left[i]         
                    i += 1                         

                elif left[i][p] > right[j][p]:   
                    myList[k] = right[j]
                    j += 1

                #Check for second or third sort level
                else:
                    if p==0:                    #Color/Size

                        if left[i][1] < right[j][1]:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i][1] > right[j][1]:   
                            myList[k] = right[j]
                            j += 1

                        else:                   #Color/Size/Fabric
                            if left[i][2] < right[j][2]:
                                myList[k] = left[i]     
                                i += 1

                            else:   
                                myList[k] = right[j]
                                j += 1

                    elif p==1:                  #Size/Fabric

                        if left[i][2] < right[j][2]:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i][2] > right[j][2]:   
                            myList[k] = right[j]
                            j += 1

                        else:                   #Size/Fabric/Color
                            if left[i][0] < right[j][0]:
                                myList[k] = left[i]     
                                i += 1

                            else:   
                                myList[k] = right[j]
                                j += 1

                    else:                       #Fabric/Color

                        if left[i][0] < right[j][0]:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i][0] > right[j][0]:   
                            myList[k] = right[j]
                            j += 1

                        else:                   #Fabric/Color/Size
                            if left[i][1] < right[j][1]:
                                myList[k] = left[i]     
                                i += 1

                            else:   
                                myList[k] = right[j]
                                j += 1
                
                k += 1                          #Move to the next slot

            else:   #DESC
                
                if left[i][p] > right[j][p]:
                    myList[k] = left[i]       
                    i += 1                       

                elif left[i][p] < right[j][p]:
                    myList[k] = right[j]
                    j += 1

                else:
                    if p==0:                    #Color/Size

                        if left[i][1] > right[j][1]:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i][1] < right[j][1]:   
                            myList[k] = right[j]
                            j += 1

                        else:                   #Color/Size/Fabric
                            if left[i][2] > right[j][2]:
                                myList[k] = left[i]     
                                i += 1

                            else:   
                                myList[k] = right[j]
                                j += 1

                    elif p==1:                  #Size/Fabric

                        if left[i][2] > right[j][2]:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i][2] < right[j][2]:   
                            myList[k] = right[j]
                            j += 1

                        else:                   #Size/Fabric/Color
                            if left[i][0] > right[j][0]:
                                myList[k] = left[i]     
                                i += 1

                            else:   
                                myList[k] = right[j]
                                j += 1

                    else:                       #Fabric/Color

                        if left[i][0] > right[j][0]:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i][0] < right[j][0]:   
                            myList[k] = right[j]
                            j += 1

                        else:                   #Fabric/Color/Size
                            if left[i][1] > right[j][1]:
                                myList[k] = left[i]     
                                i += 1

                            else:   
                                myList[k] = right[j]
                                j += 1
                            
                k += 1              

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
