import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

N, RESULT = map(int, input().split())
num_list = list(map(int, input().split()))
answer = 0

for i in range(1, N+1):
    comb = combinations(num_list, i)

    for x in comb:
        if sum(x) == RESULT:
            answer += 1

print(answer)
