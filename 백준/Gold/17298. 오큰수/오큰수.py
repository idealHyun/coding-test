import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = [-1] * N  # 처음엔 전부 -1로 둠
stack = []         # 인덱스를 저장하는 스택

for i in range(N):
    # 스택이 비어있지 않고, 현재 값(arr[i])이
    # 스택 top이 가리키는 값(arr[stack[-1]])보다 크면
    # 해당 스택 top의 오큰수는 arr[i]가 됨
    while stack and arr[stack[-1]] < arr[i]:
        top_idx = stack.pop()
        answer[top_idx] = arr[i]
    
    # 현재 인덱스를 스택에 저장
    stack.append(i)

# 스택에 남아있는 인덱스에 대해서는 기본적으로 -1 유지
print(" ".join(map(str, answer)))