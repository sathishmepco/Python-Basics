def main():
    n = int(input().strip())
    CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = (n-1)*2
    for i in range(n):
        for j in range(d-1):
            print(end=' ')
        for j in range(i,-1,-1):
            if i == n-1 and j == i:
                print(CHARS[j],end='')
            else:
                print(' '+CHARS[j],end='')
        for j in range(1,i+1,1):
            print(' '+CHARS[j],end='')
        if i == 0 and n != 1:
            print(end=' ')
        d-=2
        if i < n-1:
            print()

main()
'''
Input
5
Output
        A 
      B A B
    C B A B C
  D C B A B C D
E D C B A B C D E
'''