T = int(input())

for i in range(1,T+1):

    num_arr = list(str(i))
    is_369 = False

    for num in num_arr:
        if num in ['3','6','9']:
            is_369 = True
            print('-',end='')

    if is_369:
        print(' ',end='')
    else:
        print(i ,end=" ")