n = int(input())

data = []
for _ in range(n):
    line = list(map(int, input().split()))
    data.append(line)

# 문제 풀이
from collections import Counter

rewards=[]

for line in data:
    reward=0
    size = len(set(line))
    if(size==3):
        n = max(line)
        reward = n * 100
    elif(size==2):
        counter = Counter(line)
        if counter.most_common(1):  # most_common(1)이 비어있지 않은지 확인
            n = counter.most_common(1)[0][0]
            reward = 1000 + n * 100
    else :
        n=line[0]
        reward = 10000 + n*1000
    rewards.append(reward)

print(max(rewards))