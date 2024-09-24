# 입력 처리
import sys
N= int(sys.stdin.readline().rstrip())

string = sys.stdin.readline().rstrip()

hash=0
alphabet = []
for i,v in enumerate(string):
    hash += ((ord(v) - ord('a') + 1) * (31 ** i) % 1234567891)

print(hash)
