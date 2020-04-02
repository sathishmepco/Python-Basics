def main():
	str = input("Enter any string :: ")
	lcount = 0
	ucount = 0
	ncount = 0
	scount = 0
	for c in str:
		if c.islower():
			lcount += 1
		elif c.isupper():
			ucount += 1
		elif c.isnumeric():
			ncount += 1
		else:
			scount += 1
	print('Lowercase count -',lcount)
	print('Uppercase count -',ucount)
	print('Numeric count -',ncount)
	print('Special character count -',scount)
	
main()
'''
Enter any string :: Come@10AM
Lowercase count - 3
Uppercase count - 3
Numeric count - 2
Special character count - 1
'''