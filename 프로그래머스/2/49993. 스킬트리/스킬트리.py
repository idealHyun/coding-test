def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_arr = list(skill)
        skill_arr.reverse()
        flag=True
        for s in skill_tree:
            if s in skill_arr:
                if s!=skill_arr.pop():
                    flag=False
                    break
        if flag:
            answer+=1          
        
    return answer