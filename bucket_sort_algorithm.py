""" BUCKET SORT ALGORITHM """

#Dictionaries for conversion - ASC order
colors = {'BLUE':1, 'GREEN':2, 'INDIGO':3, 'ORANGE':4, 'RED':5, 'VIOLET':6, 'YELLOW':7}
sizes = {'L':1, 'M':2, 'S':3, 'XL':4, 'XS':5, 'XXL':6, 'XXXL':7}
fabrics = {'CASHMERE':1, 'COTTON':2, 'LINEN':3, 'POLYESTER':4, 'RAYON':5, 'SILK':6, 'WOOL':7}

def bucket_sort(myList, attr_as_str, ch):    #attr_as_str: Attribute of object as string, ch: Choice of type ascending/descending
                                
    tempList = []
    #Fill the tempList with values of objects' attributes "attr_as_str"  
    for i in range(len(myList)):
        tempList.append(getattr(myList[i], attr_as_str))

    if attr_as_str == 'color':
        #Convert strings-colors to numbers
        for i in range(len(tempList)):
            for x in colors:
                if tempList[i] == x:
                    tempList[i] = colors.get(x)
    
        tempListSort(tempList, ch)                          #Sort tempListSort ASC or DESC

        #Convert numbers to strings-colors
        for i in range(len(tempList)):
            for x in colors:
                if tempList[i] == colors.get(x):
                    tempList[i] = x

        myListSort(myList, tempList, attr_as_str, ch)       #Sort myListSort ASC or DESC

    elif attr_as_str == 'size':
        #Convert strings-sizes to numbers
        for i in range(len(tempList)):
            for x in sizes:
                if tempList[i] == x:
                    tempList[i] = sizes.get(x)

        tempListSort(tempList, ch)

        #Convert numbers to strings-sizes
        for i in range(len(tempList)):
            for x in sizes:
                if tempList[i] == sizes.get(x):
                    tempList[i] = x
                    
        myListSort(myList, tempList, attr_as_str, ch)

    else:
        #Convert strings-fabrics to numbers
        for i in range(len(tempList)):
            for x in fabrics:
                if tempList[i] == x:
                    tempList[i] = fabrics.get(x)
        
        tempListSort(tempList, ch)

        #Convert numbers to strings-fabrics
        for i in range(len(tempList)):
            for x in fabrics:
                if tempList[i] == fabrics.get(x):
                    tempList[i] = x
        
        myListSort(myList, tempList, attr_as_str, ch)
        

def tempListSort(tempList, ch):

    #Create buckets
    bucket = [None] * (max(tempList) + 1)

    #Fill all buckets with zero
    for i in range(len(bucket)):
        bucket[i] = 0

    #Fill these buckets with one where i=tempList[i]
    for i in range(len(tempList)):
        bucket[tempList[i]] += 1

    #ASC
    if (ch=="1" or ch=="3" or ch=="5"): 
        outPos = 0

    #DESC
    else:
        outPos = len(tempList) - 1 
        
    for i in range(len(bucket)):
        for j in range(bucket[i]):
            tempList[outPos] = i

            if (ch=="1" or ch=="3" or ch=="5"):
                outPos += 1

            else:
                outPos -= 1
    

def myListSort(myList, tempList, attr_as_str, ch):
    
    #Color or Size or Fabric in ASC/DESC
    a=0
    for i in range(len(tempList)-1):
        for j in range(a, len(myList)):
            if tempList[i] == getattr(myList[j], attr_as_str):
                myList[i], myList[j] = myList[j], myList[i]
                a += 1
                break
    
    #Check for second or third sort level           
    a=1
    for i in range(len(tempList)-1):
        for j in range(a, len(tempList)):
            if (tempList[i] == tempList[j]):

                if (ch=="1" or ch=="3" or ch=="5"): #ASC

                    if attr_as_str == 'color': 

                        #Color/Size
                        if myList[i].size > myList[j].size:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Color/Size/Fabric
                        elif myList[i].size == myList[j].size:
                            if myList[i].fabric > myList[j].fabric:
                                myList[i], myList[j] = myList[j], myList[i]
                    
                    elif attr_as_str == 'size':

                        #Size/Fabric
                        if myList[i].fabric > myList[j].fabric:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Size/Fabric/Color
                        elif myList[i].fabric == myList[j].fabric:
                            if myList[i].color > myList[j].color:
                                myList[i], myList[j] = myList[j], myList[i]

                    else:

                        #Fabric/Color
                        if myList[i].color > myList[j].color:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Fabric/Color/Size
                        elif myList[i].color == myList[j].color:
                            if myList[i].size > myList[j].size:
                                myList[i], myList[j] = myList[j], myList[i]

                else:   #DESC

                    if attr_as_str == 'color': 

                        #Color/Size
                        if myList[i].size < myList[j].size:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Color/Size/Fabric
                        elif myList[i].size == myList[j].size:
                            if myList[i].fabric < myList[j].fabric:
                                myList[i], myList[j] = myList[j], myList[i]
                    
                    elif attr_as_str == 'size':

                        #Size/Fabric
                        if myList[i].fabric < myList[j].fabric:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Size/Fabric/Color
                        elif myList[i].fabric == myList[j].fabric:
                            if myList[i].color < myList[j].color:
                                myList[i], myList[j] = myList[j], myList[i]

                    else:

                        #Fabric/Color
                        if myList[i].color < myList[j].color:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Fabric/Color/Size
                        elif myList[i].color == myList[j].color:
                            if myList[i].size < myList[j].size:
                                myList[i], myList[j] = myList[j], myList[i]

            else:
                break
        a+=1
