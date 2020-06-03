#This program will find out the number of square roots between the l and r range
import math
def main():
    s = input().strip().split()
    l = int(s[0])
    r = int(s[1])
    output = 0
    for i in range(l,r+1):
        rt = int(math.sqrt(i))
        if rt*rt == i:
            output += 1
    print(str(output))
main()
'''
Input
5 30
Output
3
'''
