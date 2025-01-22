def solution(user_id_list, banned_id_list):
    ban_list =[[] for _ in range(len(banned_id_list))]
    
    def compare(banned_id,user_id):
        if len(banned_id) != len(user_id):
            return False
        for i in range(len(banned_id)):
            if banned_id[i]=='*':
                continue
            elif banned_id[i]!=user_id[i]:
                return False
                
        return True
            
    
    for i,banned_id in enumerate(banned_id_list):
        for user_id in user_id_list:
            if(compare(banned_id,user_id)):
                ban_list[i].append(user_id)
                
    def count_banlist(banlist, banned_id_list):
        bad_user_data = set()

        def dfs(index, cur_set):
            if index == len(banlist):
                bad_user_data.add(tuple(sorted(cur_set)))  
                return

            for user in banlist[index]:
                if user not in cur_set: 
                    cur_set.add(user) 
                    dfs(index + 1, cur_set) 
                    cur_set.remove(user) 

        dfs(0, set())  
        return len(bad_user_data)

    return count_banlist(ban_list, banned_id_list)