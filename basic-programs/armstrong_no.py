def main():
	n = int(input('Enter the n value : '))
	temp = n
	sum = 0
	while temp > 0:
		d = temp % 10
		sum = sum + d**3
		temp = int(temp / 10)
	if sum is n:
		print('Given number',n,'is a Arimstron number')
	else:
		print('Given number',n,'is NOT a Arimstron number')
main()
'''
Enter the n value : 153
Given number 153 is a Arimstron number

Enter the n value : 120
Given number 120 is NOT a Arimstron number
'''