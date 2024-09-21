### 입력 처리
N=int(input())
numbers=sorted(list(map(int,input().split())))

### 문제 풀이
count=0

for i,n in enumerate(numbers):
    l=0
    r=N-1

    while  l<r:
        if i==l:
            l+=1
            continue
        elif i==r:
            r-=1
            continue

        if numbers[l]+numbers[r] > n :
            r-=1
        elif numbers[l]+numbers[r] < n :
            l+=1
        else :
            count+=1
            # print(n,numbers[l],numbers[r])
            break
print(count)