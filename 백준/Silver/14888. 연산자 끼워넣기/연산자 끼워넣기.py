# https://www.acmicpc.net/problem/14888
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N = int(input())
operands = list(map(int,input().split()))
operators = list(map(int,input().split()))

max_answer = - float('inf')
min_answer = float('inf')

def calculate(operator_position):
  result=operands[0]
  for i in range(N-1):
    operator = operator_position[i]
    if operator==0:
      result += operands[i+1]
    elif operator==1:
      result -= operands[i+1]
    elif operator==2:
      result *= operands[i+1]
    elif operator == 3:
      # 정수 나눗셈, 문제에 따라 음수 처리 조정 필요
      if result < 0:
          result = -(-result // operands[i + 1])
      else:
          result = result // operands[i + 1]

  return result

def make_expression(n,operator_position):
  global max_answer, min_answer

  if all(n==0 for n in operators):
    # print(operator_position)
    result = calculate(operator_position)
    # print(result)
    max_answer = max(result,max_answer)
    min_answer = min(result,min_answer)
    return
  
  for i in range(4):
    if operators[i] >=1:
      operators[i]-=1
      operator_position[n]=i
      make_expression(n+1,operator_position)
      operator_position[n]=None
      operators[i]+=1

make_expression(0,defaultdict(int))

print(max_answer)
print(min_answer)
  