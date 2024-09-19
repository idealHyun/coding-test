### 입력 처리
setting = list(map(int,input().split()))

N = setting[0] # 원래 리스트 개수
score = setting[1] # 리스트에 올릴 점수
P = setting[2] # 최종 리스트 개수

if N!=0:
    ranking = list(map(int,input().split()))
else :
    ranking=[]

### 문제 풀이
ranking.sort(reverse=True)
before_ranking=ranking[:P]

ranking.append(score)
ranking.sort(reverse=True)
top_ranking = ranking[:P]

if before_ranking == top_ranking:
    print(-1)
else :
    # 공동 등수 생각해서 등수 구하기
    for i,v in enumerate(top_ranking):
        if v==score:
            print(i+1)
            break