# 현재 체력, 최대 체력,  붕대 회복력, 붕대 소요 시간, 보너스 획복량
# 붕대 감기는 하나의 상태임
# casting, increase, bonus
# max_health, current_health
# 0 초 부터 시작
# 몬스터의 모든 타임라인이 끝난 후 남은 체력 구하기
# 만약 도중에 캐릭터 체력이 0이면 -1 반환 및 종료


# 1. 필요한 변수 초기화
# - 붕대 캐스팅시간, 증가량, 보너스
# - 현재 체력, 최대 체력
# - 붕대 경과시간
#
# 2. 전체 시뮬레이션 시간 계산
# - attaks를 순회하면서 '공격 시간'의 최대값 확인
# - 이미 정렬되어있으므로 맨 마지막 attacks의 시간 확인

# 3. 0초 부터 마지막 시간 까지 시뮬레이션
# - 처리 우선순위  공격 -> 붕대 감기 -> 보너스 처리
# - 공격 하는 상황에선느 붕대가 초기화됨

def solution(bandage, health, attacks):
    casting, increase, bonus = bandage
    current_hp, max_hp = health, health
    cast_elapsed = 0
    total_ticks = attacks[-1][0]
    
    # 시뮬레이션 처리
    attack_ticks = {tick : damage for (tick, damage) in attacks}
    for tick in range(1,total_ticks+1):
        # 공격 여부 확인 처리
        will_attack = False
        if tick in attack_ticks:
            will_attack = True
            
        # 공격 처리
        if will_attack:
            damage = attack_ticks[tick]
            current_hp -= damage
            
        
        # 플레이어 체력 확인
        if current_hp <= 0:
            return -1
        
        # 붕대 시전 취소 여부
        if will_attack:
            cast_elapsed = 0
            continue
            
        

        # 붕대 감기
        cast_elapsed += 1
        total_value = increase
        if cast_elapsed == casting:
            total_value += bonus
            cast_elapsed = 0
        
        # 체력회복시 최대 체력 클램핑
        current_hp = min(current_hp + total_value, max_hp)
    
    return current_hp 
