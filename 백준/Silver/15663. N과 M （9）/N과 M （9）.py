import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = sorted(map(int, input().split())) 
used = set() 

def dfs(values):
    if len(values) == M:
        tuple_values = tuple(values) 
        if tuple_values not in used:
            used.add(tuple_values) 
            print(" ".join(map(str, values)))
        return

    for v in arr:
        if v not in values or arr.count(v) > values.count(v):
            values.append(v)
            dfs(values)
            values.pop()

dfs([])