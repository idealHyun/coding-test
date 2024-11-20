import sys

input = lambda: sys.stdin.readline().rstrip()

word = input()
word_length = len(word)
answer='z'

# 단어를 나눌 수 있는 다양한 경우의 수 고려하기

def compare(left,middle,right):
  global answer

  left = ''.join(reversed(left))
  middle = ''.join(reversed(middle))
  right = ''.join(reversed(right))
  word2= left+middle+right

  if answer > word2:
    answer = word2


for i in range(1,word_length):
  for j in range(i+1,word_length):
    left_word = word[:i]
    middle_word = word[i:j]
    right_word = word[j:]
    compare(left_word, middle_word, right_word)

print(answer)