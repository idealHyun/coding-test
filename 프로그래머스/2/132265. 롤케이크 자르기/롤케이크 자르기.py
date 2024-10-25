def solution(topping):
    answer = 0
    
    right = dict()
    for t in topping:
        if not t in right:
            right[t]=1
        else:
            right[t]+=1
        
    left=set()
    
    for t in topping:
        left.add(t)
        
        left_size = len(left)
        
        if right[t]==1:
            right.pop(t)
        else:
            right[t]-=1
            
        right_size = len(right)
        
        if left_size == right_size:
            answer+=1
    
    return answer