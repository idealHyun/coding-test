import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 테스트 케이스의 개수

arr=(list(map(int,input().split())))

arr.sort()
min=2000000001
answer=[]
left=0
right=N-1

while left<right:
    if abs(arr[left]+arr[right]) < min:
        min = abs(arr[left]+arr[right])
        answer=[arr[left],arr[right]]
        if min==0:
            break
    else:
        if arr[left]+arr[right]<0:
            left+=1
        else:
            right-=1

for a in answer:
    print(a,end=" ")
