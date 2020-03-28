days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday',
		'Saturday','Sunday']
months = ['Jan','Feb','Mar']
print(days)
print(days[0])
print(days[1:3])
print(days[2:])
print(days + months)

print('---------------')
print('Printing all days')
for i in days:
	print(i)

num_list = [1,2,3,4,5,6]
print('---------------')
print('Printing numbers')
for i in num_list:
	print(i)
	
print('---------------')
print('Method 2')
length = len(num_list) 
for i in range(length):
	print('index ',i,'value',num_list[i]) 
	
print('---------------')
print('Using While loop')
i = 0
while i < length:
	print(num_list[i])
	i+=1

print('---------------')	
print('Method 3')
[print(i) for i in num_list] 

print('---------------')	
print('Method 4')
for i, val in enumerate(days): 
    print (i, '---',val) 
	
print('---------------')	
print('Method 5')	
print('Print list with space separated')
print(*days)
print('Print list with , separated')
print(*days, sep=",")

print('---------------')	
print('Method 6')
string = str(num_list)[1:-1]
print(string)
