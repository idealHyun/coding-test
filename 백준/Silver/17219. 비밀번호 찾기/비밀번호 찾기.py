import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int,input().split())
pwd_dict = dict()

for _ in range(N):
    k, p = input().split()
    pwd_dict[k]=p

for _ in range(M):
    k = input()
    print(pwd_dict[k])