# 입력 처리
L, C = list(map(int, input().split()))
# L : 암호의 길이
# C : 주어진 문자의 개수
characters = list(input().split())

# 암호는 사전순, 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
vowels = []  # 모음
consonants = []  # 자음

# 모음과 자음 나누기
for c in characters:
    if c in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(c)
    else:
        consonants.append(c)

import itertools

# 경우의 수를 저장할 리스트
pws = []

# 모음 n개, 자음 (L-n)개의 조합을 생성
for n in range(1, len(vowels) + 1):
    if L - n >= 2:  # 자음이 최소 2개 있어야 함
        # print(n)
        combinations_vowels = itertools.combinations(vowels, n)
        
        # 모음 조합 순회
        for comb_v in combinations_vowels:
            # print(comb_v)
            
            # 자음 조합은 매번 새롭게 생성
            combinations_consonants = itertools.combinations(consonants, L - n)
            
            # 자음 조합 순회
            for comb_c in combinations_consonants:
                pw = list(comb_v) + list(comb_c)  # 모음 + 자음 조합
                pw.sort()  # 사전순으로 정렬
                pws.append(''.join(pw))
                
pws.sort()

for pw in pws:
    print(pw)