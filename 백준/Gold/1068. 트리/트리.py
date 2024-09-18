import sys
sys.setrecursionlimit(10**6)

data = []

data.append(int(input()))

data.append(list(map(int, input().split())))

data.append(int(input()))

# print(data)

# 문제 풀이
import collections

tree=collections.defaultdict(list)

# 트리 초기화
for i in range(len(data[1])):
    tree[i]

# 트리 연결
for index,parent in enumerate(data[1]):
    if parent != -1:
        tree[parent].append(index)

# print(tree)

# 제거하는 노드가 루트 노드일 경우
if data[1][data[2]]==-1:
    print(0)
# 제거하는 노드가 루트 노드가 아닐 경우
else :
    # 부모 노드에서 제거
    tree[data[1][data[2]]].remove(data[2])

    # 자식 노드들 제거
    def remove(node):
        children = tree[node]
        for child in children:
            remove(child)
        del tree[node]
        
    remove(data[2])

    # 리프 노드 개수 세기
    count = 0

    # print(tree)

    for node in tree:
        if len(tree[node])==0:
            count+=1

    print(count)