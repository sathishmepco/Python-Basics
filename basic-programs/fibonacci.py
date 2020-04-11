def main():
	n = int(input('Enter the n value : '))
	a, b = 0, 1
	print(a,end=" ")
	print(b,end=" ")
	for i in range(2,n):
		a, b = b, a+b
		print(b,end=" ")
main()
'''
output
------
Enter the n value : 10
0 1 1 2 3 5 8 13 21 34
'''