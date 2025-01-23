# diff - level = 틀리는 횟수
# 틀리는 퍼즐 소요시간 = (이전 퍼즐 걸린 시간 + times 에서 걸리는 시간) * 틀리는 횟수 + times에서 걸리는 시간
# level 구하기
def solution(diffs, times, limit):
    def calculate_time(level):
        sol_time = 0
        for index, diff in enumerate(diffs):
            if sol_time > limit:
                return sol_time

            if level >= diff:
                sol_time += times[index]
            else:
                sol_time += (times[index] + times[index - 1]) * (diff - level) + times[index]
                
        return sol_time

    left, right = 1, max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        sol_time = calculate_time(mid)
        
        if sol_time <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer