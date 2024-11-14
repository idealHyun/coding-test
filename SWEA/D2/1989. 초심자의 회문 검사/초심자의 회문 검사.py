T = int(input())

for test_case in range(1,T+1):
    input_string = input().strip()
    answer=1

    length = len(input_string)

    for i in range(length // 2):
            if not input_string[i] == input_string[-i-1]:
                answer = 0
                break

    print(f'#{test_case} {answer}')