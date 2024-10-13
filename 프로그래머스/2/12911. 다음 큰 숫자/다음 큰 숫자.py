def count_1(n):
    count=0
    n_to_2 = []
    # 2진수로 변경
    while n!=1:
        if n%2==1:
            n_to_2.append(1)
        else:
            n_to_2.append(0)
        n= n//2
    n_to_2.append(1)
    n_to_2.reverse()
    for num in n_to_2:
        if num==1:
            count+=1
    
    return count
    

def solution(n):
    answer = 0
    n_count= count_1(n)
    while True:
        n+=1
        count=count_1(n)
        if count==n_count:
            answer=n
            break;
        
    return answer