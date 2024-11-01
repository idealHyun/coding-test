for test_case in range(1,11):
    N = int(input())
    building_arr = list(map(int,input().split()))
    count=0

    for index,buiding in enumerate(building_arr):
        if buiding==0:
            continue

        around_max = max([building_arr[index-1],building_arr[index-2],building_arr[index+1],building_arr[index+2]])

        if around_max<buiding:
            count+= buiding-around_max

    print(f'#{test_case} {count}')