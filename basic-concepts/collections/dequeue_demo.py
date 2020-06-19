from collections import deque
def main():
	d = deque('abcd')
	print('Queue of : abcd')
	for e in d:
		print(e)
	print('Add a new entry to the right side')
	d.append('e')
	print(d)
	print('Add a new entry to the left side')
	d.appendleft('z')
	print(d)	
	
	print('Return and remove the right side elt')
	print(d.pop())
	print('Return and remove the left side elt')
	print(d.popleft())
	
	print('Peek of leftmost item')
	print(d[0])
	
	print('Peek of rightmost item')
	print(d[-1])
	
	print('Reverse of deque')
	l = list(reversed(d))
	print(l)
	
	print('Search in the deque')
	bool = 'c' in d
	print(bool)
	
	print('Add multiple elements at once')
	d.extend('xyz')
	print(d)
	
	print('Right rotation')
	d.rotate(1)
	print(d)
	
	print('Left rotation')
	d.rotate(-1)
	print(d)
	
main()

'''
Queue of : abcd
a
b
c
d
Add a new entry to the right side
deque(['a', 'b', 'c', 'd', 'e'])
Add a new entry to the left side
deque(['z', 'a', 'b', 'c', 'd', 'e'])
Return and remove the right side elt
e
Return and remove the left side elt
z
Peek of leftmost item
a
Peek of rightmost item
d
Reverse of deque
['d', 'c', 'b', 'a']
Search in the deque
True
Add multiple elements at once
deque(['a', 'b', 'c', 'd', 'x', 'y', 'z'])
Right rotation
deque(['z', 'a', 'b', 'c', 'd', 'x', 'y'])
Left rotation
deque(['a', 'b', 'c', 'd', 'x', 'y', 'z'])
'''