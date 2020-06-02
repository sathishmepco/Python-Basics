import re
def main():
	n = int(input().strip())
	for i in range(n):
		no = input().strip()
		no = no.replace('-','')
		if re.match(r'[789]\d{15}$',no): 
			output = 'Valid'
		else:  
			output = 'Invalid'
		if i == n-1:
			print(output,end='')
		else:
			print(output)

main()
'''
Input
3
1234421312224231
7293-3124-5232-4231
7982214254367642
Output
Invalid
Valid
Valid
'''