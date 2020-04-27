import re

Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
num1 = '8956324712'
num2 = '1122334455'
output = Pattern.match(num1)
if output:
	print('Number 1 is valid phone number!')
else:
	print('Number 1 is invalid phone number!')
	
output = Pattern.match(num2)
if output:
	print('Number 2 is valid phone number!')
else:
	print('Number 2 is invalid phone number!')

	
'''
Number 1 is valid phone number!
Number 2 is invalid phone number!
'''