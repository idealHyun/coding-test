import sys
input = lambda: sys.stdin.readline().rstrip()

all_string = input()
bomb_string = input()
last_char = bomb_string[-1]
stack = []
len_bombstring = len(bomb_string)

for c in all_string:
    stack.append(c)
    if stack[-1] == last_char and len(stack) >= len_bombstring :
        if bomb_string == ''.join(stack[-len_bombstring:]):
            for _ in range(len_bombstring):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")