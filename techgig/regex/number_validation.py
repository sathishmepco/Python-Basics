import re
def main():
	no = input().strip()
	if re.match(r'[357]',no):   
		print('TRUE')
	else:  
		print('FALSE')  
main()
'''
Number should starts with 3, 5 or 7
63874
FALSE

349685
TRUE
'''