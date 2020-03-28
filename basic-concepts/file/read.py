import sys

try:
	file_name = 'D:\\abc.txt'
	file = open(file_name,'r')  #r for read
	
	#read first 5 characters
	print( file.read(5) )
	
	#read the first line of the file
	print( file.readline() )
	
	#reading the file
	file_content = file.read()
	print(file_content)
	
	#read the file, line by line
	for x in file:
		print(x)
		
except IOError as e:
	print('There is error in reading the file ',e)