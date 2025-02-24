N,M = map(int,input().split())
word_arr = []
for _ in range(N):
    word_arr.append(input())
    
answer = float('inf')
answer_word = ''

def compare(s1,s2):
    count = 0
    for i in range(M):
        if s1[i]!=s2[i]:
            count+=1
            
    return count

for i in range(M):
    DNA_dict = {'A':0,'C':0,'G':0,'T':0}
    max_count = 0
    dna = ''
    for j in range(N):
        DNA_dict[word_arr[j][i]]+=1
        
    for k in DNA_dict.keys():
        if DNA_dict[k] > max_count :
            max_count = DNA_dict[k]
            dna=k
            
    answer_word+=dna

answer_count = 0
for i in range(N):
    answer_count += compare(answer_word,word_arr[i])
    
print(answer_word)
print(answer_count)
        