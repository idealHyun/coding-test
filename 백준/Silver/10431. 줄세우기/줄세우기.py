### 입력 처리
n = int(input())

data=[]

for _ in range(n):
    data.append(list(map(int,input().split())))

### 문제 풀이
for index,case in enumerate(data):
    count = 0
    arr=[]
    flag=True
    for std in case[1:]:
        for s in arr:
            if s>std:
                flag=False
                i = arr.index(s)
                sliced_arr = arr[i:]
                count += len(sliced_arr)
                arr=arr[:i]+[std]+sliced_arr
                break
        if flag:
            arr.append(std)
        flag=True
    print(f"{index+1} {count}")