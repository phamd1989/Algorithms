def reverse(arr, first, last):
	while(first < last):
		swap(arr, first, last)
		first += 1
		last -= 1

def swap(arr, first, last):
	temp = arr[first]
	arr[first] = arr[last]
	arr[last] = temp

def reverseInPlace(string):
	arr = list(string)
	reverse(arr, 0, len(arr) -1)
	first = 0
	#last = 0
	i = 0
	while(i < len(arr)):
		if (arr[i] == ' '):
			reverse(arr, first, i-1)
			first = i+1
		i += 1

	# the last word
	reverse(arr, first, i-1)
	return ''.join(arr)
	#last += 1

s = 'second-to-last character, and so on. Then, go'
#
print reverseInPlace(s)