import collections

def solution(tickets):
    graph = collections.defaultdict(list) # 리스트를 기본 value로 설정
    
    # 각 출발지에서 도착지 리스트를 만들고 사전순으로 정렬
    for start, end in tickets:
        graph[start].append(end)
        
    # print(graph)
    
    # 도착지들을 사전순으로 정렬
    for key in graph:
        graph[key].sort(reverse=True)  # 스택을 사용할 것이므로 역순으로 정렬

    path = []

    def dfs(city):
        # 현재 도시에서 갈 수 있는 곳이 없을 때까지 탐색
        while graph[city]:
            next_city = graph[city].pop()  # 가장 마지막 도착지를 스택처럼 처리
            dfs(next_city)
        # print(city)
        path.append(city)  # 모든 경로를 탐색한 후 현재 도시를 경로에 추가
    
    dfs("ICN")
    
    # 결과가 거꾸로 저장되므로 역순으로 반환
    return path[::-1]