def main():
	s = input('Enter the binar string :: ').strip()
	powValue = 0
	s = s[::-1]
	decimal = 0
	for i in range(len(s)):
		v = int(s[i])
		decimal += (v * pow(2,powValue))
		powValue += 1
	print(decimal)
	
main()
'''
Enter the binar string :: 1111
15
Enter the binar string :: 1010
10
'''