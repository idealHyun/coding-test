N = int(input())
heights = list(map(int,input().split()))
results=[0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if results[j] == 0:
            if cnt == heights[i]:
                results[j] = i+1
                break
            cnt += 1

print(*results)