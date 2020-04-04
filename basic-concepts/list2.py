squares = [1,4,9,16,25]
print('Displaying the list ::',squares)
print('First element in the list ::',squares[0])
print('Last element in the list ::',squares[-1])
print('Sublist from beginning to 3rd element ::',squares[:3])
print('Sub list from index 2 element to end of the list ::',squares[2:])

list2 = [36,49,64,81,100]
print('second list ::',list2)
squares = squares + list2
print('Adding list1 and list2 ::',squares)

cubes = [1,8,27,65,125]
print('Cubes list ::',cubes)
cubes[3] = 64
print('Updating one element in the list ::',cubes)
cubes.append(216)
cubes.append(7 ** 3)
print('Appending elements to the list ::',cubes)

letters = ['a','b','c','d','e','f']
print('Letters List ::',letters)
print('Length of the letters list is ::',len(letters))
letters[2:5] = ['C','D','E']
print('After replacing some values in the list ::',letters)
letters[2:5] = []
print('Removing the upper case letters ::',letters)
letters[:] = [] # equals to letters = []
print('Clearing all the elements ::',letters)