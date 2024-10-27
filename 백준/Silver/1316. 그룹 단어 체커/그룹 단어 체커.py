import sys
input=lambda: sys.stdin.readline().strip()

N=int(input())

count=0

for _ in range(N):
    word=input()
    alphabet_dict=dict()
    prev=''
    for alphabet in word:
        if prev==alphabet:
            continue
        else:
            if alphabet in alphabet_dict.keys():
                break
            else:
                prev= alphabet
                alphabet_dict[alphabet]=True
    else:
        count+=1


print(count)