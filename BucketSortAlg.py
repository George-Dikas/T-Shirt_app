### BUCKETSORT ALGORITHM

#Dictionaries for conversion
Co = {'BLUE':1, 'GREEN':2, 'INDIGO':3, 'ORANGE':4, 'RED':5, 'VIOLET':6, 'YELLOW':7}
S = {'L':1, 'M':2, 'S':3, 'XL':4, 'XS':5, 'XXL':6, 'XXXL':7}
F = {'CASHMERE':1, 'COTTON':2, 'LINEN':3, 'POLYESTER':4, 'RAYON':5, 'SILK':6, 'WOOL':7}

def bucketSort(myList,p,ch):    #p:Position of inner list, ch:Choice of type ascending/descending

    tempList = []
    #Fill the tempList with values of position "p" 
    for i in range(len(myList)):
        tempList.append(myList[i][p])

    if(p==0):
        #Convert strings-colors to numbers
        for i in range(len(tempList)):
            for x in Co:
                if tempList[i] == x:
                    tempList[i] = Co.get(x)
    
        tempListSort(tempList,ch)           #Sort tempListSort ASC or DESC

        #Convert numbers to strings-colors
        for i in range(len(tempList)):
            for x in Co:
                if tempList[i] == Co.get(x):
                    tempList[i] = x

        myListSort(myList,tempList,p,ch)   #Sort tempListSort ASC or DESC

    elif(p==1):
        #Convert strings-sizes to numbers
        for i in range(len(tempList)):
            for x in S:
                if tempList[i] == x:
                    tempList[i] = S.get(x)

        tempListSort(tempList,ch)

        #Convert numbers to strings-sizes
        for i in range(len(tempList)):
            for x in S:
                if tempList[i] == S.get(x):
                    tempList[i] = x
                    
        myListSort(myList,tempList,p,ch)

    else:
        #Convert strings-fabrics to numbers
        for i in range(len(tempList)):
            for x in F:
                if tempList[i] == x:
                    tempList[i] = F.get(x)
        
        tempListSort(tempList,ch)

        #Convert numbers to strings-fabrics
        for i in range(len(tempList)):
            for x in F:
                if tempList[i] == F.get(x):
                    tempList[i] = x
        
        myListSort(myList,tempList,p,ch)
        

def tempListSort(tempList,ch):

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
    

def myListSort(myList,tempList,p,ch):
    
    #Color or Size or Fabric in ASC/DESC
    a=0
    for i in range(len(tempList)-1):
        for j in range(a, len(myList)):
            if (tempList[i] == myList[j][p]):
                myList[i], myList[j] = myList[j], myList[i]
                a += 1
                break
    
    #Check for second or third sort level           
    a=1
    for i in range(len(tempList)-1):
        for j in range(a, len(tempList)):
            if (tempList[i] == tempList[j]):

                if (ch=="1" or ch=="3" or ch=="5"): #ASC

                    if p==0: 

                        #Color/Size
                        if myList[i][1] > myList[j][1]:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Color/Size/Fabric
                        elif myList[i][1] == myList[j][1]:
                            if myList[i][2] > myList[j][2]:
                                myList[i], myList[j] = myList[j], myList[i]
                    
                    elif p==1:

                        #Size/Fabric
                        if myList[i][2] > myList[j][2]:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Size/Fabric/Color
                        elif myList[i][2] == myList[j][2]:
                            if myList[i][0] > myList[j][0]:
                                myList[i], myList[j] = myList[j], myList[i]

                    else:

                        #Fabric/Color
                        if myList[i][0] > myList[j][0]:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Fabric/Color/Size
                        elif myList[i][0] == myList[j][0]:
                            if myList[i][1] > myList[j][1]:
                                myList[i], myList[j] = myList[j], myList[i]

                else:

                    if p==0: 

                        #Color/Size
                        if myList[i][1] < myList[j][1]:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Color/Size/Fabric
                        elif myList[i][1] == myList[j][1]:
                            if myList[i][2] < myList[j][2]:
                                myList[i], myList[j] = myList[j], myList[i]
                    
                    elif p==1:

                        #Size/Fabric
                        if myList[i][2] < myList[j][2]:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Size/Fabric/Color
                        elif myList[i][2] == myList[j][2]:
                            if myList[i][0] < myList[j][0]:
                                myList[i], myList[j] = myList[j], myList[i]

                    else:

                        #Fabric/Color
                        if myList[i][0] < myList[j][0]:
                            myList[i], myList[j] = myList[j], myList[i]

                        #Fabric/Color/Size
                        elif myList[i][0] == myList[j][0]:
                            if myList[i][1] < myList[j][1]:
                                myList[i], myList[j] = myList[j], myList[i]

            else:
                break
        a+=1
