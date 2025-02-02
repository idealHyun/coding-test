import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()

def dfs(depth,values):
    if depth == M:
        for v in values:
            print(v,end=' ')
        print()
        return

    for i in arr:
        if not values or values[-1] <= i:
            values.append(i)
            dfs(depth+1,values)
            values.pop()

dfs(0,[])

