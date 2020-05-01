def main():
    n = int(input().strip())
    d = (n-1)*2
    for i in range(n):
        for j in range(d-1):
            print(end=' ')
        for j in range(i,-1,-1):
            if i == n-1 and j == i:
                print(str(j),end='')
            else:
                print(' '+str(j),end='')
        for j in range(1,i+1,1):
            print(' '+str(j),end='')
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
        0 
      1 0 1
    2 1 0 1 2
  3 2 1 0 1 2 3
4 3 2 1 0 1 2 3 4
'''