matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
    [9, 10, 11, 12],
]
print('Displaying the Matrix')
print(matrix)

transposed = []
for i in range(4):
	transposed.append([row[i] for row in matrix])
print('Transpose of the Matrix')
print(transposed)

print('Alternate way of Transpose')
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

list(zip(*matrix))
