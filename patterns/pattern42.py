def main():
    n = int(input().strip())
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n-1,-1,-1):
        for j in range(5):
            if j == 0:
                print(CHARS[i],end='')
            else:
                print(' '+CHARS[i],end='')
        if i != 0:
            print()
main()
'''
Input
5
Output
E E E E E
D D D D D
C C C C C
B B B B B
A A A A A
'''