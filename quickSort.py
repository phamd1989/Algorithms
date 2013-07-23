import sys
# sorting the array using quicksort around a pivot value
# separate method for choosing the pilot value
# function takes in an array, its left and right indexes
# separate method for partitioning the array around the pivot value
# recurse on the left and right parts around the pivot

def quickSort(arr, left, right):
	global count
	# base case
	if (left>=right):		
		return
	# recursive method
	pivot = choosePivotPos(arr, left, right)
	pivotPoint = partition(arr, pivot, left, right)
	#arr = pivotPoints[2]
	# print 'count: ', count
	# print 'pivotPoint: ', pivotPoint
	# print '___________________________'

	# why count here don't work???????
	quickSort(arr, left, pivotPoint - 1)
	#count += pivotPoint - 1 - left	
	quickSort(arr, pivotPoint + 1, right)
	#count += right - pivotPoint - 1
	return arr

def choosePivotPos(arr, left, right):
	# can be tweaked
	#print left, right
	size = right - left + 1
	#med = -1
	#print 'size: ', size
	if (size%2 == 0):
		med = left + size/2 -1
	else:
		med = left + size/2

	return left
	# return right
	#print med, arr
	#print 'chooseMedian(arr, left, med, right): ', chooseMedian(arr, left, med, right)
	# return chooseMedian(arr, left, med, right)

def chooseMedian(arr, left, med, right):
	l = arr[left]
	m = arr[med]
	r = arr[right]

	if (l < m):
		if (m < r): # l<m<r
			return med
		else: #l<m m>r
			if l<r:
				return right
			else:
				return left

	else: #l>m
		if (m>r):
			return med
		else: # m<r, l>m
			if (l<r):
				return left
			else:
				return right

def partition(arr, pivot, left, right):
	#print arr
	# moving the value at pivot to the first value of the array
	#print arr
	global count
	count += right - left
	# print left, right
	swap(arr, left, pivot)
	#print arr
	i, j = left + 1, left + 1
	while(j <= right):
		if (arr[j] < arr[left]):
			swap(arr, j, i)			
			i += 1
		j += 1
	#print i, j
	#print arr
	# return the value at pivot to its correct location
	swap(arr, left, i-1)
	# print arr
	# print i - 1
	return i-1

def swap(arr, i, j):
	temp = arr[j]
	arr[j] = arr[i]
	arr[i] = temp

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

def main():
	global count 
	count = 0
	arr = readInput()
	#print arr
	#swap(arr, 1, 2)
	#count += len(arr)-1
	quickSort(arr, 0, len(arr)-1)
	print count

main()