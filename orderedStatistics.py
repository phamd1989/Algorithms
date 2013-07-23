#find k-th ordered element in an array without sorting it first

# choose pivot and partition the array around the pivot value
# determine what part we need to partition to find the k-th element
# remember to update the k-th value appropriately

def orderedStatistics(arr, left, right, pos):

	# recursion
	# partition the array around the pivot value, 1st element
	pivotPos = partition(arr, left, right)
	print 'pivotPos: ', pivotPos
	print 'pos: ', pos
	#
	if (pos == pivotPos + 1):

		return arr[pivotPos]
	elif (pos <= pivotPos + 1):
		return orderedStatistics(arr, left, pivotPos - 1, pos)
	else:
		print 'go here'
		return orderedStatistics(arr, pivotPos + 1, right, pos)

def partition(arr, left, right):
	print arr
	pivot = arr[left]
	i, j = left + 1, left + 1
	while(j <= right):
		if (arr[j] < pivot):
			swap(arr, j, i)
			i += 1
		j += 1
	# move pivot to its correct location
	print i-1
	swap(arr, left, i-1)
	print arr
	return i-1

def swap(arr, j, i):
	temp = arr[j]
	arr[j] = arr[i]
	arr[i] = temp


print orderedStatistics([9,5,3,8,4,1,2,7,6,10], 0, 9, 6)