### 입력 처리
# 1 ≤ N ≤ 15
# 0 ≤ r, c < 2^N
# N은 지수, r행 c열이 몇번째인지
N,r,c = list(map(int,input().split()))

### 문제 풀이
count =0
arr=[]

min_r=0
min_c = 0

for n in range(N,0,-1):
    length= 2 ** n / 2
    nr = min_r + length
    nc = min_c + length

    if r < nr and c < nc:
        arr.append(0)
    elif r < nr and c >= nc:
        min_c = nc
        arr.append(1)
    elif r >= nr and c < nc:
        min_r=nr
        arr.append(2)
    elif r >= nr and c >= nc:
        min_r=nr
        min_c = nc
        arr.append(3)

for i,v in enumerate(arr):
    count+= v* 2 ** ((N-i) *2 -2)

print(count)