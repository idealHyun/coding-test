import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 도시 개수

road_length=(list(map(int,input().split())))
oil_value=(list(map(int,input().split())))

answer=0

for i in range(N-2,-1,-1):
    min=float('inf')
    for k in range(i+1):
        if min>oil_value[k]:
            min=oil_value[k]
    answer+=min*road_length[i]

print(answer)

