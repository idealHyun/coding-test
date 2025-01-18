import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer=[]

def backtracking():
    if len(answer)==M:
        print(" ".join(map(str,answer)))
        return

    for i in arr:
        if i not in answer:
            answer.append(i)
            backtracking()
            answer.pop()

backtracking()
