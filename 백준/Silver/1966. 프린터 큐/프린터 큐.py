import sys
input=lambda: sys.stdin.readline().strip()

from collections import deque

T=int(input())

for _ in range(T):
    N,M=map(int,input().split())

    importance=list(map(int,input().split()))
    sorted_importance=deque(sorted(importance,reverse=True))
    q=deque([i for i in range(N)])

    count=0
    flag=False

    while q:
        n = sorted_importance.popleft() # 가장 높은 중요도 꺼내기
        count+=1

        # q의 내용 돌면서 n의 중요도이면 빼고, 아니면 뒤로 넣기
        for i in range(N):
            k= q.popleft()
            if importance[k]!=n:
                q.append(k)
            else:
                if M==k:
                    flag=True
                break
        
        if flag:
            break
    
    print(count)


    
