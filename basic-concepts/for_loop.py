#for loop
print('------Looping through string list')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x,len(x))

print('------Looping through String')
str = 'Python'
for x in str:
	print(x)

print('-----Range() function')
for x in range(10):
	print(x)
	
print('-----Range() function with start and end value')
for x in range(2,5):
	print(x)

print('-----Range() function with start, end, step')
for x in range(1,10,2):
	print(x)
	
print('-----Range() with negative numbers')
for x in range(-10, -100, -30):
	print(x)
	
print('-----for with else block')
for x in range(5):
	print(x)
else:
	print('For block is over')
	
print('-----nested for loops')
for i in range(3):
	for j in range(3):
		print(i,j)

print('-----print list items using range()')
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
	print(i,fruits[i])
	
print('-----print(range(5))')
print(range(5))

print('-----sum(print(range(5)))')
print(sum(range(5)))

print('-----list(range(5))')
print(list(range(5)))