def main():
    n = int(input().strip())
    for i in range(n):
        for j in range(n-i):
            if j == 0:
                print(end='*')
            else:
                print(end=' *')
        if i < n-1:
            print()
main()
'''
Input
5
Output
* * * * *
* * * *
* * *
* *
*
'''