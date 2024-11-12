T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    num_list = [False for i in range(10)]
    
    temp_N=N
    while True:
        str_N = str(temp_N)
        for n in str_N:
            num_list[int(n)]=True

        if not False in num_list:
            break
        temp_N += N

    print(f'#{test_case} {temp_N}')
