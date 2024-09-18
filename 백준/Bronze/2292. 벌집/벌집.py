### 입력 처리
data = int(input())

### 문제 풀이
count =1

while data-1>0:
    data-=count*6
    count+=1

print(count)