def main():
    n = int(input('Enter the n value : ').strip())
    for i in range(n):
        for j in range(n):
            print(str(i+1),end='')
            if j < n-1:
                print(end=' ')
        if i < n-1:
            print("")
main()

'''
Enter the n value : 5
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

Enter the n value : 3
1 1 1
2 2 2
3 3 3
'''