# convert a string to a number
def atoi(string):
	result = 0
	negative = False

	if (string[0] == '-'):
		negative = True
	
	for ch in string:
		if (ch != '-'):
			result = result * 10 + int(ch)
	if negative:
		return -result
	return result

print atoi('0')

# converst a number to a string
def itoa(number):
	result = []
	negative = False
	if (number == 0):
		return '0'

	if (number < 0):
		negative = True
		number = -number

	while(number != 0):
		result.insert(0, str(number%10))
		number = number/10
		#print number

	if negative:
		result.insert(0, '-')

	return ''.join(result)

print itoa(1322433535)



