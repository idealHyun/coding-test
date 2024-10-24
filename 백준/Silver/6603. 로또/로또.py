import sys
input=lambda: sys.stdin.readline().strip()

import itertools

arr=[]

while True:
    line = list(map(int,input().split()))
    if line[0]==0:
        break
    arr.append(line)

for line in arr:
    k=line[0]
    nums=line[1:]
    
    combs = itertools.combinations(nums,6)
    for a in combs:
        print(' '.join(map(str, a)))
    print()