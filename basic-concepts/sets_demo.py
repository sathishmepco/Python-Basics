fruitsSet = {"apple", "banana", "cherry"}
print('Displaying the set :',fruitsSet)

print('Loop through the set:')
for x in fruitsSet:
	print(x)
	
if "banana" in fruitsSet:
	print('Yes banana is present in the list')

fruitsSet.add('orange')
print('Orange is added to the set')

fruitsSet.update(["orange", "mango", "grapes"])
print('Adding multiple fruits :',fruitsSet)

print('Length of the fruits set :',len(fruitsSet))
fruitsSet.remove("banana")
print('banana is removed from the set :',fruitsSet)

fruitsSet.discard("apple")
print('apple is removed using discard method :',fruitsSet)

fruitsSet.clear()
print('Clearing the set :',fruitsSet)

del fruitsSet
#fruitsSet is not defined
#print('Delete the set :',fruitsSet)

'''
Displaying the set : {'cherry', 'apple', 'banana'}
Loop through the set:
cherry
apple
banana
Yes banana is present in the list
Orange is added to the set
Adding multiple fruits : {'cherry', 'orange', 'apple', 'mango', 'banana', 'grapes'}
Length of the fruits set : 6
banana is removed from the set : {'cherry', 'orange', 'apple', 'mango', 'grapes'}
apple is removed using discard method : {'cherry', 'orange', 'mango', 'grapes'}
Clearing the set : set()
'''