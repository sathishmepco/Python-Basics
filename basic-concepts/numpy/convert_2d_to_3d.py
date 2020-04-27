import numpy as np
def main():
    #s = input().strip().split()
    s = '1 2 3 4 5 6 7 8 9'.split()
    arr = np.array([])
    for i in range(len(s)):
        v = int(s[i])
        arr = np.append(arr,v)
    arr = np.reshape(arr,(3,3))
    ss = np.array2string(arr,precision=0, separator=' ',suppress_small=True)
    ss = ss.replace('.','')
    print(ss,end='')

main()

'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''