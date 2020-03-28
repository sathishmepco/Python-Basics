import os

if os.path.exists('D:\\abc.txt'):
	os.remove('D:\\abc.txt')
	print('File successfully deleted!')
else:
	print('The file does not exist!')
