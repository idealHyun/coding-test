import sys
input=lambda: sys.stdin.readline().strip()

import itertools
import math

N=int(input())

arr=[]
players=[]

for i in range(1,N+1):
    arr.append(list(map(int,input().split())))
    players.append(i)

combinations = itertools.combinations(players,N//2)

min=float('inf')

for combination in combinations:
    start_members=combination
    link_members=players.copy()
    for member in combination:
        link_members.remove(member)

    start_combinations = itertools.combinations(start_members,2)
    link_combinations = itertools.combinations(link_members,2)

    start=0
    link=0

    for sc in start_combinations:
        start += arr[sc[0]-1][sc[1]-1] + arr[sc[1]-1][sc[0]-1]
    
    for lc in link_combinations:
        link += arr[lc[0]-1][lc[1]-1] + arr[lc[1]-1][lc[0]-1]

    diff = abs(start - link)
    
    if diff<min:
        min=diff

print(min)
