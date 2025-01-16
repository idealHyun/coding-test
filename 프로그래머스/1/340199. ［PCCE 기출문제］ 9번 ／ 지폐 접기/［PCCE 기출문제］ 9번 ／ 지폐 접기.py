def solution(wallet, bill):
    answer = 0
    
    while max(bill) > max(wallet) or min(bill) > min(wallet):
        bill_max = max(bill)
        bill.remove(bill_max)
        bill.append(bill_max//2)
        answer+=1
    
    return answer