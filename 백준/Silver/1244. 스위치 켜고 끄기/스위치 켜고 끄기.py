### 입력 처리
n = int(input()) # 스위치 개수

switch = list(map(int,input().split())) # 스위치 상태

std_n = int(input()) # 학생 수

std_arr=[] # 학생 배열 [성별, 스위치 번호]
for std in range(std_n):
    std_arr.append(list(map(int,input().split())))

### 문제 풀이

for std in std_arr :
    sex = std[0] # 성별
    num = std[1] # 받은 스위치 번호
    if sex==1:
        i=num -1
        while(i<len(switch)):
            switch[i] = 1 if switch[i]==0 else 0
            i=i+num
    else:
        i=num-1
        j=0
        is_equal=True
        switch[i]=1 if switch[i]==0 else 0
        while is_equal:
            j+=1
            if i-j>=0 and i+j<len(switch):
                prev=switch[i-j]
                next=switch[i+j]
                if prev==next:
                    switch[i-j]=1 if switch[i-j]==0 else 0
                    switch[i+j] =1 if switch[i+j]==0 else 0
                else:
                    is_equal=False
            else :
                break

for i in range(0, len(switch), 20):
    print(" ".join(map(str, switch[i:i+20])))