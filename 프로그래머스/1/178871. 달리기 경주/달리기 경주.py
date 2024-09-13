def solution(players, callings):
    playerMap = {};
    
    for i in range(0, len(players)):
        playerMap[players[i]] = i
    
    for calling in callings:
        index=playerMap.get(calling)
        [players[index-1],players[index]]=[players[index],players[index-1]]
        
        playerMap[players[index]] = index
        playerMap[players[index-1]] = index - 1
    
    return players