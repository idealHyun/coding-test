import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures.sort(key=lambda x: x[1])

heap = []

for lecture in lectures:
    n, start, end = lecture

    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))