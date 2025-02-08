import bisect

def solution(A, B):
    answer = 0
    B.sort()
    
    for a in A:
        i = bisect.bisect_right(B,a)
        if i!=len(B):
            del B[i]
            answer+=1
    
    return answer