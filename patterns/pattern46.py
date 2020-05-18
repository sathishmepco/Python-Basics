def main():
    n = int(input().strip())
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(5):
            if j == 0:
                print(CHARS[i],end='')
            else:
                print(' '+CHARS[i],end='')
        if i != n-1:
            print()
main()
'''
Input
5
Output
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
'''