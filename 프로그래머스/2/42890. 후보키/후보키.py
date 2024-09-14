import itertools

def solution(relation):
    candidate = []
    columnNum = len(relation[0])
    
    candidateKeys = []

    for i in range(1, columnNum + 1):
        # 현재 속성 개수 i에 대해 가능한 모든 속성 조합을 생성
        combinations = list(itertools.combinations(range(columnNum), i))
        # print(combinations)

        # 개수를 늘려가며 최소성 확인하며 중복되는거 있는지 확인
        for combination in combinations:
            textSet = set()  # 각 조합에 대해 새로운 textSet 생성
            for relationIndex in range(len(relation)):
                text = ""  # 각 행에 대해 새로운 text 생성
                for combinationIndex in combination:
                    text += relation[relationIndex][combinationIndex]
                    # print(text)
                textSet.add(text)  # 조합된 문자열을 집합에 추가
                # print(textSet)

            if len(textSet) == len(relation):  # 유일성 검사
                candidateKeys.append(set(combination))
                # print("현재 후보키",candidateKeys)
    
    # 최소성 검사를 위해 복사본을 생성
    candidateKeysCopy = candidateKeys.copy()

    # 최소성 검사: 후보키 중 부분집합 관계에 있는 후보키 제거
    for i in range(len(candidateKeys)):
        for j in range(i + 1, len(candidateKeys)):
            key1 = candidateKeys[i]
            key2 = candidateKeys[j]
            # key1이 key2의 부분집합인 경우, key2는 최소성을 만족하지 않으므로 제거
            if key1.issubset(key2):
                try:
                    candidateKeysCopy.remove(key2)  # key2를 후보키 목록에서 제거
                except:
                    continue

    return len(candidateKeysCopy)
