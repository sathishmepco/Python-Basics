#Print all the factors of a given number
def main():
	num = int(input('Enter the integer value :: '))
	factors = []
	for i in range(1,int(num/2)+1):
		if num % i is 0:
			factors.append(i)
	factors.append(num)
	print('The factors are :',factors)
	
main()

'''
OUTPUT
------
Enter the integer value :: 50
The factors are : [1, 2, 5, 10, 25, 50]

Enter the integer value :: 49
The factors are : [1, 7, 49]

Enter the integer value :: 41
The factors are : [1, 41]

Enter the integer value :: 60
The factors are : [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
'''