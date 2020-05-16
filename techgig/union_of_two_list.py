def main():
    n1 = int(input()) 
    A = list(map(int,input().strip().split()))[:n1] 
    n2 = int(input()) 
    B = list(map(int,input().strip().split()))[:n2] 
    A = set(A)
    B = set(B)
    C = A.__or__(B)
    print(len(C),end='')
main()

'''
Input
4
1 2 3 5
3
2 8 9
Output
6
'''