def main():
    n = int(input()) 
    A = list(map(int,input().strip().split()))[:n] 
    n = int(input()) 
    B = list(map(int,input().strip().split()))[:n] 
    A = set(A)
    B = set(B)
    C = A.symmetric_difference(B)
    for i in C:
        print(i)

main()
'''
Input
3
1 3 5 
4
2 3 5 6 
Output
1
2
6
'''