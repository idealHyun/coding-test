def solution(prices):
    n= len(prices)
    answer = [0] * n
    stack = [] 

    for i in range(n):
        while stack and stack[-1][0] > prices[i]:
            price, idx = stack.pop()
            answer[idx] = i - idx
        stack.append((prices[i], i))

    while stack:
        price, idx = stack.pop()
        answer[idx] = n - 1 - idx

    return answer