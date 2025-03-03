import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

def draw_star(n):
  if n==1:
    return ['*']

  star = draw_star(n//3)
  answer = []

  for s in star:
    answer.append(s*3)
  for s in star:
    answer.append(s + ' '*(n//3) + s)
  for s in star:
    answer.append(s*3)

  return answer

print('\n'.join(draw_star(N)))