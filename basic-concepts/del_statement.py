a = [-1, 1, 66.25, 333, 333, 1234.5]
print('The elements in the list are :',a)
del a[0]
print('After deleting 0th index element :',a)
del a[2:4]
print('Deleting elements from index 2 to 4th element')
print('After deletion :',a)
del a[:]
print('Deleting entire list :',a)

'''
OUTPUT
------
The elements in the list are : 		[-1, 1, 66.25, 333, 333, 1234.5]
After deleting 0th index element :	[1, 66.25, 333, 333, 1234.5]
Deleting elements from index 2 to 4th element
After deletion : 					[1, 66.25, 1234.5]
Deleting entire list : 				[]
'''