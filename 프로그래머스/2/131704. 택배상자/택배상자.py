def solution(orders):
    answer = 0
    length = len(orders)
    orders.reverse()
    stack=[]
    n=1
    
    while orders:
        next=orders.pop()
        # print(next)
        
        while n<length+1:
            # print("n값",n)
            if next==n:
                # print("if문 일치")
                answer+=1
                if n<length:
                    n+=1
                break
            elif stack and next==stack[-1]:
                stack.pop()
                # print("스택에서 일치")
                answer+=1
                break
            else:
                if stack and next<stack[-1]:
                    # print(stack)
                    # print("못함")
                    return answer
                else:
                    stack.append(n)
                    # print("스택에 추가")
                    # print(stack)
            if n<length:
                    n+=1
    return answer
            
