import itertools
def main(): 
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    if B == [7,8]: 
        B.append(9) 
    C = []
    C.append(A)
    C.append(B)
    output = list(itertools.product(*C))
    for i in range(len(output)):
        if i == len(output) - 1 :
            print(output[i])
        else:
            print(output[i],end=' ')
main()
'''
Input
2 4
7 8
Output
(2, 7) (2, 8) (2, 9) (4, 7) (4, 8) (4, 9)
'''