### 입력 처리
N=int(input())
numbers=list(map(int,input().split()))

### 문제 풀이

if N==1 :
    numbers.sort()
    sum=0
    for n in numbers[:5]:
        sum+=n
    print(sum)
else :
    min_arr=[]

    for i in range(3):
        min_arr.append(min(list([numbers[i],numbers[-(i+1)]])))

    min_arr.sort()
    min_1 = min(min_arr)
    min_2 = 0
    min_3=0
    for i,v in enumerate(min_arr):
        if(i<2):
            min_2 += v
        min_3+=v

    sum=0
    sum += min_3 *4
    sum += min_2 * ((N-2) * 8 +4)
    sum+= min_1 * (N-2) * (5*N -6)
    print(sum)
