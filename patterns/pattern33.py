def main():
    n = int(input().strip())
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(n-i):
            if j == 0:
                print(CHARS[i],end='')
            else:
                print(' '+CHARS[i],end='')
        if i < n-1:
            print()
main()
'''
Input
5
Output
A B C D E
A B C D
A B C
A B
A
'''