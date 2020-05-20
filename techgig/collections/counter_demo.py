from collections import Counter
def main():
    n = int(input().strip())
    l = list(map(int,input().strip().split()))
    c = Counter(l)
    print(c)
main()

'''
Input
10
1 2 3 2 4 3 2 1 1 4
Output
Counter({1: 3, 2: 3, 3: 2, 4: 2})
'''