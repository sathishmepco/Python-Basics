def print_rangoli(size):
    #n = int(input().strip())
    n = size
    incr = -1
    a = n-1
    alphas = "abcdefghijklmnopqrstuvwxyz"
    for i in range((2*n)-1):
        for j in range(a):
            print('--',end='')
        for j in range(n-1,a,-1):
            print(alphas[j],end='-')
        print(alphas[a],end='')
        for j in range(a+1,n,1):
            print('-'+alphas[j],end='')
        for j in range(a):
            print('--',end='')
        print('')
        a += incr
        if a == 0:
            incr = 1

n = int(input().strip())
print_rangoli(n)
'''
Sample Input
5
Sample Output
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''