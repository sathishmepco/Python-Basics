import math
def main(): 
	AB = int(input()) 
	BC = int(input())
	print(90-int(round(math.degrees(math.atan(AB/BC)))),end='')
main()
'''
Input
6
6
Output
45
'''