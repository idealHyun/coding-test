import sys
import math

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    num = int(input())
    count=0
    for i in range((num//3) +1):
        r_i=num-3*i
        for j in range((r_i//2) +1):
            r_j=r_i-2*j
            k=i+j+r_j
            if k>0:
                temp=math.comb(k,i)
                if k>0:
                    temp*=math.comb(k-i,j)
                if k>0:
                    temp*=math.comb(k-i-j,r_j)
                count+=temp
    print(count)