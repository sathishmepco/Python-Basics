def main():

    n = int(input().strip())
    names = []
    heights = []
    for i in range(n):
        names.append(input().strip())
        heights.append(int(input().strip()))
    maxv = heights[0]
    smax = heights[1]
    if maxv < smax:
        maxv = heights[1]
        smax = heights[0]
    for i in range(2,n,1):
        if heights[i] != maxv:
            if maxv < heights[i]:
                smax = maxv
                maxv = heights[i]
            elif smax < heights[i]:
                smax = heights[i];
        
    output = []
    for i in range(n):
        if smax == heights[i]:
            output.append(names[i])
    output.sort()
    for i in range(len(output)):
        if i < len(output) - 1:
            print(output[i])
        else:
            print(output[i],end='')

main()

'''
Input
-----
4
saurabh 
102
arpit
120
aditya
102
varun
101

Output
------
aditya
saurabh
'''