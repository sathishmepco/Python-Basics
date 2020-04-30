def main():
    n = int(input().strip())
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = (n-1)*2
    for i in range(n):
        for j in range(d-1):
            print(end=' ')
        for j in range(i+1):
            if i == n-1 and j == 0:
                print(CHARS[j],end='')
            else:
                print(' '+CHARS[j],end='')
        for j in range(i-1,-1,-1):
            print(' '+CHARS[j],end='')
        d-=2
        if i < n-1:
            print()

main()
'''
Input
5
Output
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
'''