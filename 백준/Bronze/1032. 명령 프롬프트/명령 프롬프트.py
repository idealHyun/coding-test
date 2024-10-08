import sys
input=lambda: sys.stdin.readline().strip()

N=int(input())

answer=[]

arr=[]

for _ in range(N):
    arr.append(input())

for i in range(len(arr[0])):
    char=arr[0][i]
    answer.append(char)
    for j in range(1,N):
        if char!=arr[j][i]:
            answer[i]='?'
            break

print(''.join(answer))