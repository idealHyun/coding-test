import sys
input=lambda: sys.stdin.readline().strip()

N = int(input())
origin_arr = list(map(int,input().split()))
origin_arr.sort()

M = int(input())
target_arr = list(map(int,input().split()))

def find(target):
    s=0
    e=len(origin_arr)-1

    while s<=e:
        mid = (s+e) //2

        if origin_arr[mid]<target:
            s=mid+1
        elif origin_arr[mid]>target:
            e=mid -1
        elif origin_arr[mid]==target:
            return 1
    
    return 0

for target in target_arr:
    print(find(target))