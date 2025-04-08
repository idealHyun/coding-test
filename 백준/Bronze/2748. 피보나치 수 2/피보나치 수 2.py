import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    a, b = 0, 1
    for _ in range(2, N + 1):
        a, b = b, a + b
    print(b)