#This program will give you distinct prime factors of a number
import math
def main():
    T = int(input().strip())
    for t in range(T):
        n = int(input().strip())
        limit = int(math.sqrt(n))
        factors = []
        for i in range(2,limit+1):
            while n%i == 0:
                factors.append(i)
                n = n/i
        if n > 2:
            factors.append(int(n))
        distinct_factors = set(factors)
        distinct_factors = sorted(distinct_factors)
        print(len(distinct_factors))
        for id,val in enumerate(distinct_factors):
            if id == len(distinct_factors)-1:
                print(val,end=' \n')
            else:
                print(val,end=' ')
main()
'''
Input
2
15
40
Output
2
3 5 
2
2 5 
'''