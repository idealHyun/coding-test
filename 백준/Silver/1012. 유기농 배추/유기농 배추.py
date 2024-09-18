import sys
sys.setrecursionlimit(10**6)

n = int(input())

data = []
for _ in range(n):
    case =[]
    case.append(list(map(int, input().split())))
    for _ in range(case[0][2]):
        case.append(list(map(int, input().split())))
    data.append(case)

# print(data)

# 문제 풀이

for graph in data:
    count =0
    xs = graph[0][0]
    ys = graph[0][1]

    visited = [[False] * xs for _ in range(ys)]

    for i in range(1,len(graph)):
        visited[graph[i][1]][graph[i][0]]=True

    # 상-> 우-> 하-> 좌
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]

    def dfs(x,y):
        if visited[y][x]:
            visited[y][x]=False
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if nx>=0 and nx<xs and ny>= 0 and ny<ys:
                    dfs(nx,ny)
        

    for i in range(1,len(graph)):
        if visited[graph[i][1]][graph[i][0]]:
            dfs(graph[i][0],graph[i][1])
            count +=1

    print(count)