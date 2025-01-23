import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int,input().split())

def dfs(depth,cur_list):
    if depth==M:
        print(' '.join(map(str,cur_list)))
        return
    
    for i in range(1,N+1):
        cur_list.append(i)
        dfs(depth+1,cur_list)
        cur_list.pop()

dfs(0,[])
