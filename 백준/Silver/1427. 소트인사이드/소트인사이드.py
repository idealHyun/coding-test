import sys
input=lambda: sys.stdin.readline().strip()

num=list(input())

num.sort(reverse=True)

print(''.join(num))