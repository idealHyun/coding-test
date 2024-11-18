import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
n=0
k=0

while(True):
  if n * (n+1) // 2 >= N :
    break
  else:
    n+=1

b = n * (n+1) // 2 - N

if n % 2 ==0:
  print(f'{n - b}/{1+ b }')
else:
  print(f'{1+ b }/{n - b}')