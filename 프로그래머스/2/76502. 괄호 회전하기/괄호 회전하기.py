def solution(s):
    answer = 0
    length=len(s)
    for i in range(length):
        stack="";
        for j in range(length):
            k=(j+i)%length
            stack+=s[k]
            if(len(stack)>1):
                text=stack[-2:]
                if text in ['[]', '()', '{}']:
                    stack=stack[:-2]
        if len(stack)==0:
            answer+=1
            
    return answer