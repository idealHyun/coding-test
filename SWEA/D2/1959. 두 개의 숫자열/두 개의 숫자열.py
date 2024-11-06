from collections import deque

T = int(input())

for test_case in range(1,T+1):
    N,M = map(int,input().split())

    n_arr = list(map(int,input().split()))
    m_arr = list(map(int,input().split()))

    answer = - float('inf')

    def compare(long_arr,short_arr):
        global answer

        long_length = len(long_arr)
        short_length = len(short_arr)
        diff_length = long_length-short_length

        for i in range(diff_length +1):
            cut_long_arr = long_arr[i:short_length+i]
            num_sum = 0
            
            for j in range(short_length):
                num_sum += short_arr[j] * cut_long_arr[j]

            if num_sum>answer:
                answer=num_sum

    if N>M:
        compare(n_arr,m_arr)
    else:
        compare(m_arr,n_arr)

    
    print(f'#{test_case} {answer}')