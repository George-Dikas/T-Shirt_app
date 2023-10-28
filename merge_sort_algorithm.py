""" MERGE SORT ALGORITHM """

def merge_sort(myList, attr_as_str, ch):        #attr_as_str: Attribute of object as string, ch: Choice of type ascending/descending     
    
    if len(myList) > 1:                         #If list has more than one element
        mid = len(myList) // 2                  #finding the mid of the list
        left = myList[:mid]                     #Left half of the list
        right = myList[mid:]                    #Right half of the list

        merge_sort(left,attr_as_str,ch)         #Sorting the first half
        merge_sort(right,attr_as_str,ch)        #Sorting thr second half

        i = j = 0                               #Two iterators for traversing the two halves
        k = 0                                   #Iterator for the main list
        
        while i < len(left) and j < len(right):

            if ch=="1" or ch=="3" or ch=="5":   #ASC  
            
                if getattr(left[i], attr_as_str) < getattr(right[i], attr_as_str):
                    myList[k] = left[i]         
                    i += 1                         

                elif getattr(left[i], attr_as_str) > getattr(right[i], attr_as_str):   
                    myList[k] = right[j]
                    j += 1

                #Check for second or third sort level in case of '=='
                else:
                    if attr_as_str == 'color':                    #Color/Size

                        if left[i].size < right[j].size:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i].size > right[j].size:   
                            myList[k] = right[j]
                            j += 1

                        else:                                       #Color/Size/Fabric
                            if left[i].fabric < right[j].fabric:
                                myList[k] = left[i]     
                                i += 1

                            elif left[i].fabric > right[j].fabric:   
                                myList[k] = right[j]
                                j += 1

                            else:
                                break

                    elif attr_as_str == 'size':                  #Size/Fabric

                        if left[i].fabric < right[j].fabric:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i].fabric > right[j].fabric:   
                            myList[k] = right[j]
                            j += 1

                        else:                   #Size/Fabric/Color
                            if left[i].color < right[j].color:
                                myList[k] = left[i]     
                                i += 1

                            elif left[i].color > right[j].color:   
                                myList[k] = right[j]
                                j += 1

                            else:
                                break

                    else:                                           #Fabric/Color

                        if left[i].color < right[j].color:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i].color > right[j].color:   
                            myList[k] = right[j]
                            j += 1

                        else:                   #Fabric/Color/Size
                            if left[i].size < right[j].size:
                                myList[k] = left[i]     
                                i += 1

                            elif left[i].size > right[j].size:   
                                myList[k] = right[j]
                                j += 1
                                
                            else:
                                break
                                
                k += 1                                              #Move to the next slot

            else:   #DESC
                
                if getattr(left[i], attr_as_str) > getattr(right[i], attr_as_str):
                    myList[k] = left[i]       
                    i += 1                       

                elif getattr(left[i], attr_as_str) < getattr(right[i], attr_as_str):
                    myList[k] = right[j]
                    j += 1

                #Check for second or third sort level in case of '=='
                else:
                    if attr_as_str == 'color':                    #Color/Size

                        if left[i].size > right[j].size:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i].size < right[j].size:   
                            myList[k] = right[j]
                            j += 1

                        else:                   #Color/Size/Fabric
                            if left[i].fabric > right[j].fabric:
                                myList[k] = left[i]     
                                i += 1

                            elif left[i].fabric < right[j].fabric:   
                                myList[k] = right[j]
                                j += 1

                            else:
                                break

                    elif attr_as_str == 'size':                  #Size/Fabric

                        if left[i].fabric > right[j].fabric:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i].fabric < right[j].fabric:   
                            myList[k] = right[j]
                            j += 1

                        else:                   #Size/Fabric/Color
                            if left[i].color > right[j].color:
                                myList[k] = left[i]     
                                i += 1

                            elif left[i].color < right[j].color:  
                                myList[k] = right[j]
                                j += 1

                            else:
                                break

                    else:                                           #Fabric/Color

                        if left[i].color > right[j].color:
                            myList[k] = left[i]     
                            i += 1

                        elif left[i].color < right[j].color:   
                            myList[k] = right[j]
                            j += 1

                        else:                                       #Fabric/Color/Size
                            if left[i].size > right[j].size:
                                myList[k] = left[i]     
                                i += 1

                            elif left[i].size < right[j].size:   
                                myList[k] = right[j]
                                j += 1

                            else:
                                break
                            
                k += 1                                              #Move to the next slot              

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
