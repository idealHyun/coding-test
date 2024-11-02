# T = int(input())

for test_case in range(1,11):
    C = int(input())
    box_arr = list(map(int,input().split()))
    box_arr.sort()
    min_height=0
    count = 0

    while count<C:
        if box_arr[-1]-box_arr[0] <=1:
            break

        box_arr[-1] -=1
        box_arr[0]+=1
        box_arr.sort()

        count+=1

    min_height = box_arr[-1]-box_arr[0]

    print(f'#{test_case} {min_height}')