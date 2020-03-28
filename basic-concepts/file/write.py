import sys

#appending to file
try:
	file_name = 'D:\\abc.txt'
	file = open(file_name,'a')	#a for appending to file
	file.write('Learning Python!')
	file.write('\n')
	file.close()
except IOError as e:
	print('There is error in writing the file ',e)
finally:
	if file is not None:
		file.close()
	
#writing to file, this will erase the previous content
try:
	file_name = 'D:\\abc.txt'
	file = open(file_name,'w')	#w write to file
	file.write('Writing to file!')
	file.write('\n')
	file.close()
except IOError as e:
	print('There is error in writing the file ',e)
finally:
	if file is not None:
		file.close()
