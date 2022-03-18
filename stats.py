def funcMean(list): #mean function using list elements
    noOfElem = len(list) #check list length
    totalSum = 0 #totalSum variable initialization
    if noOfElem == 0:
        return 0 #return zero if empty
    else:
        for num in list: #for loop for the sum calculation of list
            totalSum += num
        aveMean = totalSum/noOfElem #total sum over number of Elements
        return aveMean #return Mean

def funcMedian(list): #median function using list elements
    noOfElem = len(list)
    if noOfElem == 0: #check list length
        return 0 #return zero if empty
    else:
        list.sort() #sort the list
        numMid = noOfElem // 2 #finding the middle number/s by division of 2
        if noOfElem%2 == 0:
            return (list[numMid] + list[numMid - 1 ]) / 2 #if length = even, average the mid values
        else:
            return list[numMid] #if length = odd, average the mid value    

def funcMode(list): #mode function using list elements
    count = {} #count and numHigh_most initialization
    numHigh_most = 0
    for i in list: #using list elements as keys for dictionary creation
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 1 #dictionary iteration
    for i in count.keys():
        if count[i] > numHigh_most:
            numHigh_most = count[i] #assigning highest number of occurences
            aveMode = i
    return aveMode #return mode

def main(): #main function
    list = [45, 66, 22,10,15,88,15,31,90] #elements of the list
    print("List: ", list)
    print("Mean: ", funcMean(list))
    print("Median: ", funcMedian(list))
    print("Mode: ", funcMode(list))

#process start    
main()
#process end