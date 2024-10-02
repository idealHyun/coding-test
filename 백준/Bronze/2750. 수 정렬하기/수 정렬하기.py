import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 테스트 케이스의 개수

arr=[]

for _ in range(N):
    arr.append(int(input()))

arr.sort()

for n in arr:
    print(n)
