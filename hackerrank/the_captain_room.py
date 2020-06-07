def main():
	k = int(input().strip())
	s = input().strip().split()
	roomList = {}
	for i in range(len(s)):
		v = int(s[i])
		if v in roomList:
			roomList[v] = roomList[v]+1
		else:
			roomList[v] = 1
	for key,value in roomList.items():
		if value == 1:
			print(str(key))
main()
'''
Sample Input
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
Sample Output
8
'''