import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [input() for _ in range(N)]

arr.sort(key=lambda a: (len(a), sum(int(c) for c in a if c.isdigit()), a))

for a in arr:
  print(a)
