def main():
    n = int(input().strip())
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(4,-1,-1):
            if j == 4:
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
E D C B A
E D C B A
E D C B A
E D C B A
'''