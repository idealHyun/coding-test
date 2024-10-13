from collections import deque

def solution(bandage, health, attacks):
    answer=health
    turn = 0
    health_turn=0
    attacks_arr = deque(attacks)
    band_max_turn, second_coverage, plus_coverage = bandage
    # 공격을 먼저 체크 (0이면 죽기) -> 공격 없으면 회복 -> 회복 연속 성공 확인 -> 체력 최대까지만 회복
    while attacks_arr:
        attack_turn,attack_damage = attacks_arr.popleft()
        while turn!=attack_turn:
            turn +=1
            health_turn+=1
            if health_turn ==band_max_turn:
                answer+=second_coverage + plus_coverage
                health_turn=0
            else:
                answer += second_coverage
            if answer> health:
                answer=health
        answer -=attack_damage
        if answer <1 :
            break;
        health_turn=0
        turn+=1
        
    if answer>0:
        return(answer)
    else:
        return(-1)