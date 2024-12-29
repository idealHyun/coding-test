import collections

def solution(cacheSize, cities):
    answer = 0
    
    cache = ["" for _ in range(cacheSize)]
    
    q = collections.deque(cache)
    for city in cities:
        city = city.lower()
        if city in q:
            answer+=1
            q.remove(city)
            if cacheSize > 0:
                q.append(city)
        else:
            answer+=5
            if cacheSize > 0 and len(q)==cacheSize:
                q.popleft()
                q.append(city)
    
    return answer