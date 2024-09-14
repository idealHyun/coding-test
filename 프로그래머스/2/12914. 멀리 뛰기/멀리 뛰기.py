import math

def solution(n):
    answer = 0
    two_max_count= n // 2 # 2칸 최대 개수
    
    for i in range(two_max_count+1):
        one_count = n - i * 2
        total_count=one_count+i
        answer+=math.comb(total_count,i)
        
    return answer % 1234567