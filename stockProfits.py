# given a list of stock prices on different dates
# figure out a pair of dates: buy first, sell second
# which yields the maximum profit

def maxProfits(arr, left, right):
	middle = (left+right)/2
	leftArr = arr[left:middle+1]
	rightArr = arr[middle+1:right+1]
	return leftArr, rightArr

print maxProfits([2,4,5,7], 0, 3)