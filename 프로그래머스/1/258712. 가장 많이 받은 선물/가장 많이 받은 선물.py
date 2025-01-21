def solution(friends, gifts):
    answer = 0
    gift_dict = dict() # 선물 지수
    gift_history = dict() # 선물 내역
    gift_answer = dict() # 최종 선물 받은 개수
    
    for friend in friends:
        gift_dict[friend]=0
    
    for gift in gifts:
        sender, receiver = gift.split(' ')
        gift_history[gift] = gift_history.get(gift, 0) + 1
        gift_dict[sender]+=1
        gift_dict[receiver]-=1
    
    for i in range(len(friends)):
        recevied_gift=0
        for j in range(i,len(friends)):
            a_name =friends[i]
            b_name =friends[j]
            a = gift_history.get(f'{a_name} {b_name}',0)
            b = gift_history.get(f'{b_name} {a_name}',0)
            
            if a>b:
                gift_answer[a_name]=gift_answer.get(a_name,0) +1
            elif b>a :
                gift_answer[b_name]=gift_answer.get(b_name,0) +1
            else:
                a_num = gift_dict.get(a_name)
                b_num = gift_dict.get(b_name)
                if a_num > b_num:
                    gift_answer[a_name]=gift_answer.get(a_name,0) +1
                elif b_num > a_num:
                    gift_answer[b_name]=gift_answer.get(b_name,0) +1
                    
    for key in gift_answer:
        if answer < gift_answer.get(key):
            answer = gift_answer.get(key)
    
    return answer

# 선물 기록이 있으면, 더 많은 선물을 받은 사람이 선물 받음
# 선물지수 = 준 선물 수 -받은 선물 수
# 선물 기록이 없거나 같으면, 선물 지수가 높은 사람이 선물 받음
# 선물 지수 같으면 계산X
