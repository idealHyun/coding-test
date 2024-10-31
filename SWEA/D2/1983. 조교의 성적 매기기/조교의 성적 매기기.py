T = int(input())

RESULT=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for test_case in range(1,T+1):
    N,K = map(int,input().split())
    std_arr=[]
    target_score=0

    for std in range(1,N+1):

        m,f,h = map(int,input().split())
        sum_score = m*0.35 + f*0.45 + h*0.2

        if std==K:
            target_score=sum_score

        std_arr.append(sum_score)

    std_arr.sort(reverse=True)
    index=std_arr.index(target_score)

    print(f'#{test_case} {RESULT[index // (N//10)]}')