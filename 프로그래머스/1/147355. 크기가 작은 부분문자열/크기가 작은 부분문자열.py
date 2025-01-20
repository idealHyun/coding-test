def solution(t, p):
    answer = 0
    total_length = len(t)
    length = len(p)
    for i in range(total_length-length+1):
        if int(t[i:i+length]) <= int(p):
            answer+=1
    return answer