import sys

def inversionList(arr):
    size = len(arr)
    if (size == 1):
        return arr
    low_arr = arr[0:size/2]
    high_arr = arr[size/2:size]
    return mergeAndCount(inversionList(low_arr), inversionList(high_arr))

def mergeAndCount(low_arr, high_arr):
    global count 
    combined_arr = []
    l = len(low_arr)
    r = len(high_arr)
    i, j = 0, 0
    while(i<l and j<r):
        if (low_arr[i] < high_arr[j]):
            combined_arr.append(low_arr[i])
            i = i + 1
        else:
            combined_arr.append(high_arr[j])
            j += 1
            count += l - i
    while(i<l):
        combined_arr.append(low_arr[i])
        i += 1
    while(j<r):
        combined_arr.append(high_arr[j])
        j += 1
    return combined_arr

def readInput():
    inputArray = []
    inFile = sys.argv[1]
    try:
        myInput = open(inFile, 'r')
        while (True):
            num = myInput.readline().strip()
            if (len(num) == 0):
                break
            inputArray.append(int(num))
    finally:
        myInput.close()
    return inputArray

count = 0
inputArr = readInput()
#print inputArr
inversionList(inputArr)
print count

