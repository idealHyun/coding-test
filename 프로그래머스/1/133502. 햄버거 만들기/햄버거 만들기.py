def solution(ingredient):
    answer = 0
    stack =""
    for i in ingredient:
        stack += str(i)
        if(i==1):
            text=stack[-4:]
            if(text=="1231"):
                stack=stack[:-4]
                answer+=1
    return answer