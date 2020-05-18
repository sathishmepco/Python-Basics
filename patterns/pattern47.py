def main():
    n = int(input().strip())
    for i in range(n):
        for j in range(1,6):
            if j == 1:
                print(str(j),end='')
            else:
                print(' '+str(j),end='')
        if i < n-1:
            print()
main()
'''
Input
5
Output
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''