def main():
    n = int(input().strip())
    d = (n-1)*2
    for i in range(n):
        for j in range(d-1):
            print(end=' ')
        for j in range(i+1):
            if i == n-1 and j == 0:
                print(str(j+1),end='')
            else:
                print(' '+str(j+1),end='')
        for j in range(i-1,-1,-1):
            print(' '+str(j+1),end='')
        d-=2
        if i < n-1:
            print()

main()
'''
Input
5
Output
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''