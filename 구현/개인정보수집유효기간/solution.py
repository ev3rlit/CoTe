# 목표 : 오늘 날짜를 기준으로 파기해야하는 개인 정보 번호
# 개인정보는 유효기간 expired_at이 존재
# 모든 달은 28일로 통일 -> 12 * 28  = 336
# 각 유저마자 유효기간이 다름
# 현재 날짜
# 2000년 1월 1일 부터 사용자의 정보 수집 일수 확인
# 2000년 1월 1일 부터 오늘날짜 까지 총 일수 확인
# 일수 차이가 유효기간 보다 높은 항목의 인덱스를 반환, 오름차순

# 입력 크기
# 최대 크기가 100이므로 순회 가능

# 1. 상태 초기화
# - terms_map : 각 약관의 유효기간
# - 2000년 1월 1일 부터 오늘까지 기간 차이 = 총일수
# 2. privacies 순회
# - 기준일자로 부터 수집일자 일 수 계산 = 경과일수
# - 총일수 - 경과일수 >= 유효일수 보다 큰 경우 제거 대상

def get_days(a):
    a_year,a_month,a_day = a
    b_year,b_month,b_day = (2000, 1, 1)
    
    days = 0
    
    days += (a_year - b_year) * 336
    days += (a_month - b_month) * 28
    days += (a_day - b_day)
    
    return days

def to_date(a):
    return tuple(map(int,a.split('.')))

def solution(today, terms, privacies):
    answer = []
    
    # 1. 상태 초기화
    terms_map = {term : int(month) * 28 for (term, month) in map(str.split, terms)}
    total_days = get_days(to_date(today))
    
    # 2. 순회
    for (i, privacy) in enumerate(privacies):
        created_at, term = privacy.split()
        created_at = to_date(created_at)
        elapsed = get_days(created_at)
        
        duration = terms_map[term]
        if total_days - elapsed >= duration:
            answer.append(i+1)
            
    return sorted(answer)