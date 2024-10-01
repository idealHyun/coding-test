import sys
input = lambda: sys.stdin.readline().rstrip()

H,W = map(int, input().split())

heights=list(map(int, input().split()))

sum=0

for i,v in enumerate(heights):
    left_max=v
    right_max=v

    for j in range(i-1,-1,-1):
        if heights[j]>left_max:
            left_max=heights[j]

    for k in range(i+1,W):
        if heights[k]>right_max:
            right_max=heights[k]
    
    h=min(left_max,right_max)

    sum+= h-v

print(sum)