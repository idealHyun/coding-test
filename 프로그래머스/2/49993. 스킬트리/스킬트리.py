def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_arr = list(skill)[::-1]
        for s in skill_tree:
            if s in skill_arr and s!=skill_arr.pop():
                break
        else:
            answer+=1          
        
    return answer