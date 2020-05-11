def main():
    n = int(input().strip())
    for i in range(n):
        for j in range(n,i,-1):
            if j == n:
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
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''