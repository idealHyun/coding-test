import math

def solution(number, limit, power):
    answer = 1
    
    def count_divisor(n):
        count=0
        for i in range(1,int(math.sqrt(n))+1):
            if n % i == 0:
                count +=2
                if n // i == i:
                    count -=1
        
        return count
    
    for i in range(2,number+1):
        divisor_count = count_divisor(i)
        if divisor_count > limit:
            answer += power
        else:
            answer += divisor_count
        
    return answer