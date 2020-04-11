def main():
	start = int(input('Enter the start value : '))
	end = int(input('Enter the end value : '))
	primeNos = []
	for value in range(start,end+1):
		flag = True
		for j in range(2,int(value/2)):
			if value % j == 0:
				flag = False
				break
		if flag is True:
			primeNos.append(value)

	for i in range(len(primeNos)):
		if i is len(primeNos)-1:
			print(primeNos[i],end="")
		else:
			print(primeNos[i],end=",")
main()