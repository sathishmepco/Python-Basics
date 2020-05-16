import itertools
def main():
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
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
3 5
Output
(2, 3) (2, 5) (4, 3) (4, 5)
'''