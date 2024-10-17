import re

def solution(s):
    answer = []
    arr = re.findall(r'\{([^{^}]*)\}', s)
    arr.sort(key=len)
    num_dict={}
    
    for s in arr:
        arr2=s.split(',')
        for n in arr2:
            if not n in num_dict.keys():
                num_dict[n]=True
                answer.append(int(n))
    return answer