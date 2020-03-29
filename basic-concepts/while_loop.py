#While loop
print('Print 1 to 10')
i = 1
while i < 10:
	print(i)
	i += 1

print('Break at 5')	
i = 1
while i < 10:
	print(i)
	if i == 5:
		break
	i += 1
	
print('While loop with else block')	
i = 1
while i < 5:
	print(i)
	i += 1
else:
	print('While block is exited when i become ',i)