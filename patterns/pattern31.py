def main():
    n = int(input().strip())
    for i in range(n):
        for j in range(n-i):
            if j == 0:
                print(str(n-i),end='')
            else:
                print(' '+str(n-i),end='')
        if i < n-1:
            print()
main()
'''
Input
5
Output
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''