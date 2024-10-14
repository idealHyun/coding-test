def solution(record):
    answer = []
    user_dict={}
    result=[]
    for line in record:
        command = list(line.split())
        # print(behavior, uid, nickname)
        if command[0]=="Enter":
            user_dict[command[1]]=command[2]
            result.append((command[0],command[1]))
        elif command[0]=="Change":
            user_dict[command[1]]=command[2]
        else :
            result.append((command[0],command[1]))
    
    for i in result:
        behavior, uid = i
        if behavior=="Enter":
            answer.append(f"{user_dict[uid]}님이 들어왔습니다.")
        else :
            answer.append(f"{user_dict[uid]}님이 나갔습니다.")
    
    return answer