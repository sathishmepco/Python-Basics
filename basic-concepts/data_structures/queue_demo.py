from collections import deque
queue = deque(["Eric", "John", "Michael"])
print('The items in the queue are :',queue)
queue.append("Terry")
print('After appending Terry :',queue)
queue.append("Graham")          
print('After appending Graham :',queue)
print('Pop the item from the queue :',queue.popleft())
print('After Pop :',queue)
print('Pop the item from the queue :',queue.popleft())
print('After Pop :',queue)

'''
OUTPUT
------
The items in the queue are : deque(['Eric', 'John', 'Michael'])
After appending Terry : deque(['Eric', 'John', 'Michael', 'Terry'])
After appending Graham : deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
Pop the item from the queue : Eric
After Pop : deque(['John', 'Michael', 'Terry', 'Graham'])
Pop the item from the queue : John
After Pop : deque(['Michael', 'Terry', 'Graham'])
'''