import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
c_dict = dict()
max_pay = 0

for i in range(N):
    days, pay = map(int,input().split())
    c_dict[i]=(days,pay)

def dfs(cur_date,cur_pay,next_pay):
    global max_pay
    if cur_date >= N:
        if cur_date == N:
            cur_pay += next_pay
        max_pay = max(max_pay, cur_pay)
        return

    cur_pay += next_pay
    dfs(cur_date+c_dict[cur_date][0],cur_pay,c_dict[cur_date][1])
    dfs(cur_date+1,cur_pay,0)
    
dfs(0,0,0)    

print(max_pay)