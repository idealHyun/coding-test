def solution(nums):
    answer = 0
    pSet=set(nums);
    if(len(pSet)>=len(nums)/2):
        return len(nums)/2
    else :
        return len(pSet)