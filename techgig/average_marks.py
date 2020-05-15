def main():
    n = int(input().strip())
    marks = list(map(float,input().strip().split()))[:n] 
    avg = sum(marks) / n
    print("{:.3f}".format(avg))
main()
'''
Input
5
145 147 150 145 145
Output
145.400
'''