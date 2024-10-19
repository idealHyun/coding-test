def solution(n):
    answer = 0
    for i in range(1,n+1):
        sum=0
        num=i
        while sum <=n:
            if n==sum:
                answer+=1
                break
            else:
                sum+=num
            num+=1
    
    return answer