import sys
import collections

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
people=collections.defaultdict(list)

for _ in range(N):
  person = list(input().split())
  people[person[0]].append(person[1])

key_list = sorted(list(map(int,people.keys())))

for key in key_list:
  for name in people[str(key)]:
    print(f'{key} {name}')