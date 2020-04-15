array = [23,32,43,25,52,35]
print('Original List values :',array)
array.sort()
print('After sorting :',array)
array.reverse()
print('Reverse the list :',array)
temp = [25,23]
array.extend(temp)
print('Add another list at end of the list :',array)
print('How many time 25 is present in the list :',array.count(25))
array.insert(0,10)
print('Insert 10 at 0th index :',array)
print('Max value in the list :',max(array))
print('Min value in the list :',min(array))
array.remove(23)
print('Remove the first occurance of 23 :',array)
array.pop()
print('Remove the last element :',array)
del array[2]
print('Remove the item in the index 2 :',array)
array.clear()
print('Clearing the list :',array)

'''
OUTPUT
------
Original List values : 					[23, 32, 43, 25, 52, 35]
After sorting : 						[23, 25, 32, 35, 43, 52]
Reverse the list : 						[52, 43, 35, 32, 25, 23]
Add another list at end of the list : 	[52, 43, 35, 32, 25, 23, 25, 23]
How many time 25 is present in the list : 2
Insert 10 at 0th index : 				[10, 52, 43, 35, 32, 25, 23, 25, 23]
Max value in the list : 				52
Min value in the list : 				10
Remove the first occurance of 23 : 		[10, 52, 43, 35, 32, 25, 25, 23]
Remove the last element : 				[10, 52, 43, 35, 32, 25, 25]
Remove the item in the index 2 : 		[10, 52, 35, 32, 25, 25]
Clearing the list : 					[]
'''