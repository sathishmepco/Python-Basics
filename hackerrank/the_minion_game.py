def minion_game(string):
	n = len(string)
	stuart = 0
	kevin = 0
	for i in range(n):
		if string[i] not in "AEIOU":
			stuart += n-i
		else:
			kevin += n-i
	if stuart > kevin:
		print('Stuart '+str(stuart))
	elif kevin > stuart:
		print('Kevin '+str(kevin))
	else:
		print('Draw')
minion_game("BANANA")

'''
Sample Input
BANANA

Sample Output
Stuart 12
'''