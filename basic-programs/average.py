import re
def main():
	n = int(input('Enter the n value: '))
	string = input('Enter the n integers with space separated : ').strip()
	sarray = re.split('\s',string)
	list = []
	for i in range(n):
		value = int(sarray[i])
		list.append(value)
	totalSum = sum(list)
	avg = totalSum / n
	print(avg)
	print("{0:.2f}".format(avg))
main()