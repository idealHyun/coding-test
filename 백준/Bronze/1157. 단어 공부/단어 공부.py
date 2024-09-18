### 입력 처리
data = input()

### 문제 풀이
from collections import Counter

counter = Counter(data.upper())
if len(counter)>1:
    first, second = counter.most_common(2)

    if first[1]==second[1]:
        print("?")
    else :
        print(first[0])
else :
    print(counter.most_common(1)[0][0])

