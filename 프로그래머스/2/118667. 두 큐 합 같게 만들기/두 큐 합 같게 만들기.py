from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    total = sum_q1 + sum_q2

    if total % 2 == 1:
        return -1

    target = total // 2
    max_operations = len(queue1) * 3
    operations = 0

    while operations <= max_operations:
        if sum_q1 == target:
            return operations
        
        if sum_q1 > target:
            value = q1.popleft()
            q2.append(value)
            sum_q1 -= value
            sum_q2 += value
        else:
            value = q2.popleft()
            q1.append(value)
            sum_q1 += value
            sum_q2 -= value
        
        operations += 1

    return -1 
