def main():
    n = int(input().strip())
    s = input().strip().split()
    s = list(dict.fromkeys(s))
    maxv = int(s[0])
    smax = int(s[1])
    if maxv < smax:
        maxv = int(s[1])
        smax = int(s[0])
    for i in range(2,len(s),1):
        v = int(s[i])
        if v > maxv:
            smax = maxv
            maxv = v
        elif v > smax:
            smax = v
    print(smax)

main()
'''
Input
5
3 9 9 5 4 
Output
5
'''