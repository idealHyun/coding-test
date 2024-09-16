import itertools

def solution(clothes):
    answer = 0
    clothes_dict={}
    
    # 데이터 처리
    for cloth in clothes:
        key = cloth[1]
        value = cloth[0]
        if key in clothes_dict:
            clothes_dict[key].append(value)
        else :
            clothes_dict[key] = [value]
            
    # print(clothes_dict)
    # 경우의 수 구하기
    answer = 1
    for key in clothes_dict:
        # 해당 의상 종류에서 선택할 수 있는 경우의 수는 (해당 의상 개수 + 1)
        # +1은 해당 의상 종류를 선택하지 않는 경우도 포함
        answer *= (len(clothes_dict[key]) + 1)
    return answer -1 # 아무것도 안 입은 경우 빼기