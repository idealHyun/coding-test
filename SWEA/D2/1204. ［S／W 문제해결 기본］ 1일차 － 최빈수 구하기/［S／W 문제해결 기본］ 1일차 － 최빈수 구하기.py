T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    score_dict=dict()

    score_list = list(map(int,input().split()))

    max_score =0
    max_frequency = 0

    for score in score_list:
        if score in score_dict.keys():
            score_dict[score]+=1
        else:
            score_dict[score]=1

        frequency = score_dict.get(score)
        if max_frequency<frequency:
            max_frequency = frequency
            max_score=score
        elif max_frequency==frequency and max_score<score: 
            max_score=score
    
    print(f'#{test_case} {max_score}')