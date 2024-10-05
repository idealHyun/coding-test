import sys
input=lambda: sys.stdin.readline().strip()

N=int(input())
arr= list(map(int,input().split()))

M=int(input())
targets=list(map(int,input().split()))

answer={}
for t in targets:
    answer[t]=0

arr.sort()
sorted_targets=sorted(targets)

arr_index=0
sorted_targets_index=0
while arr_index<len(arr) and sorted_targets_index<len(sorted_targets):

    if sorted_targets[sorted_targets_index]==arr[arr_index]:
        answer[sorted_targets[sorted_targets_index]]+=1
        arr_index+=1
    elif sorted_targets[sorted_targets_index]<arr[arr_index]:
        sorted_targets_index+=1
    else:
        arr_index+=1

for target in targets:
    print(answer[target],end=" ")