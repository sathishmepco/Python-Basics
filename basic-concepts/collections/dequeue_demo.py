from collections import deque
def main():
	d = deque('abcd')
	print('Queue of : abcd')
	for e in d:
		print(e)
	d.append('e')
	d.appendleft('z')
	print(d)	
main()

'''

'''