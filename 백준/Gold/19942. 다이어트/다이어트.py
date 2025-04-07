# https://www.acmicpc.net/problem/19942
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
mp, mf,ms,mv = map(int,input().split())
foods = []
for i in range(N):
  p, f, s, v, price = map(int, input().split())
  # (음식번호, 단백질, 지방, 탄수화물, 비타민, 가격)
  foods.append((i+1, p, f, s, v, price))

min_price = float('inf')
answer_foods = set()

# 인덱스 ,현재 영양수치, 가격, 포함된 음식 번호
def dfs(index, sum_nutrients, sum_price, include_foods):
  global min_price, answer_foods

  np,nf,ns,nv = sum_nutrients
  if np>=mp and nf>=mf and ns >= ms and nv >= mv and min_price >= sum_price:
    if min_price == sum_price:
        temp =sorted(include_foods.copy())
        answer_foods.add(tuple(temp))
    else:
        min_price = sum_price
        answer_foods.clear()
        temp =sorted(include_foods.copy())
        answer_foods.add(tuple(temp))
    return
  
  if index >= N:
     return
  
  dfs(index + 1, (np, nf, ns, nv), sum_price, include_foods)
  dfs(index + 1, (np+foods[index][1],nf+foods[index][2],ns+foods[index][3],nv+foods[index][4]),sum_price+foods[index][5],include_foods + [foods[index][0]])

dfs(0,(0,0,0,0), 0, [])

if min_price != float('inf'):
  temp_foods = sorted(answer_foods)  
  result = temp_foods[0]           
  print(min_price)
  print(' '.join(map(str, result)))
else:
   print(-1)