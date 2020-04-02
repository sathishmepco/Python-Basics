def main():
	str = input('Enter any string :: ')
	str = str.lower();
	vowelsCount = 0
	for vowel in 'aeiou':
		count = str.count(vowel)
		vowelsCount += count
		conCount = len(str) - vowelsCount
	print('Vowels Count -',vowelsCount,'Consonants Count -',conCount)

main()