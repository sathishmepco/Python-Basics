def main():
    n = int(input().strip())
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(n-1,i-1,-1):
            if j == n-1:
                print(CHARS[j],end='')
            else:
                print(' '+CHARS[j],end='')
        if i < n-1:
            print()
main()
'''
Input
5
Output
E D C B A
E D C B
E D C
E D
E
'''