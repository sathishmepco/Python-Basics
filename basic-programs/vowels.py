def main():
	str = input('Enter any string :: ')
	str = str.lower();
	vowel_counts = {}
	for vowel in 'aeiou':
		count = str.count(vowel)
		vowel_counts[vowel] = count
	print(vowel_counts)
main()
'''
Enter any string :: aeiou
{'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
'''