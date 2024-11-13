T = int(input())

for test_case in range(1,T+1):
    input_string = input()

    for i in range(1,11):
        for n in range(i):
            if not input_string[n]==input_string[n+i]:
                break
        else:
            print(f'#{test_case} {i}')
            break