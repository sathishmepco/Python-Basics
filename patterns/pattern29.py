def main():
    n = int(input().strip())
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(n-1,i-1,-1):
            if j == n-1:
                print(CHARS[n-i-1],end='')
            else:
                print(' '+CHARS[n-i-1],end='')
        if i < n-1:
            print()
main()
'''
Input
5
Output
E E E E E
D D D D
C C C
B B
A
'''