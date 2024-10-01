import sys
input = lambda: sys.stdin.readline().rstrip()

from heapq import heappop,heappush
N = int(input())
hq=[]

for _ in range(N):
    start,end = map(int,input().split())
    heappush(hq,(end,start))

start=0
end=0
count=0

while hq:
    e,s=heappop(hq)
    if end<=s:
        end=e
        count+=1
    
print(count)