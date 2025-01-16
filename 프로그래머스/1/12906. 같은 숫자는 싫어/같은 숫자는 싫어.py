def solution(arr):
    answer = []
    for item in arr:
        if len(answer) ==0:
            answer.append(item)
        else:
            if item != answer[-1]:
                answer.append(item)
    
    return answer