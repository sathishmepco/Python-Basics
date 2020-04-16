fruits = ("apple", "banana", "cherry")
print('Displaying tuple :',fruits)

print('Looping through tuple using for loop ::')
for i in range(len(fruits)):
	print(fruits[i])

print('Alternate approach :')
for x in fruits:
	print(x)

if "apple" in fruits:
	print("Yes, 'apple' is in the fruits tuple")
