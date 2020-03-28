#factorial program
def factorial(n):
	if(n == 1):
		return 1
	else:
		return n * factorial(n-1)

num = int(input('Enter the integer value :: '))
if num < 0:
	print('Sorry enter the positive integer')
elif num is 0:
	print('Factorial of 0 is 1')
else:
	print('Factorial of ',num,' is ',factorial(num))