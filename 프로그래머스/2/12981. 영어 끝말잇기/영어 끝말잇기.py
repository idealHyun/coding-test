import math

def solution(n, words):
    dict={}
    for index,word in enumerate(words):
        num=(index+1)%n
        if num == 0:
            num = n
        turn= math.ceil((index+1)/n)
        # 끝말잇기 탈락
        if index>0 and words[index-1][-1] !=word[0]:
            return [num,turn]
        # 중복 탈락
        if word in dict.keys():
            return [num,turn]
        else :
            dict[word]=True

    return [0,0]