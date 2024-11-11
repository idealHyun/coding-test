import sys
input = lambda: sys.stdin.readline().rstrip()

N=int(input())

for i in range(N,0,-1):
  print('*' * i)