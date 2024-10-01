import sys
input = lambda: sys.stdin.readline().rstrip()

N = input()
n=N
flag=True
count=0

while flag:
    if int(n)<10:
        n="0"+n

    first=str(int(n[0])+int(n[1]))
    second=n

    if len(first)==1:
        first_num=first[0]
    else:
        first_num=first[1]

    second_num=second[1]

    n=second_num+first_num

    n=str(int(n))

    count+=1

    if n==N:
        flag=False

print(count)