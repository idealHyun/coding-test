T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ingredient_count, limit_kcal = map(int,input().split())
    ingredients=[]
    answer = 0

    for _ in range(ingredient_count):
        ingredients.append(list(map(int,input().split())))

    def dfs(i, score, kcal):
        global answer
        
        if kcal > limit_kcal:
            return
        if answer < score:
            answer = score
        if i==ingredient_count:
            return
        
        dfs(i+1,score + ingredients[i][0], kcal + ingredients[i][1])
        dfs(i + 1, score, kcal )

    dfs(0,0,0)

    print(f'#{test_case} {answer}')