import os
import sys

def getMoneySpent(keyboards, drives, b):
    keyboards = sorted(keyboards,reverse=True)
    drives = sorted(drives,reverse=True)
    spent = -1
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i]+drives[j] <= b:
                if spent < keyboards[i]+drives[j]:
                    spent = keyboards[i]+drives[j]
                break
    return spent

bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
moneySpent = getMoneySpent(keyboards, drives, b)
print(str(moneySpent))

'''
10 2 3
3 1
5 2 8
'''