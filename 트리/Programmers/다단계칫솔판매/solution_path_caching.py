"""
경로 캐싱 방식들을 비교하는 파일
"""

from collections import defaultdict

# ============================================================
# 방법 1: 현재 방식 (딕셔너리 조회)
# ============================================================
def solution_dict(enroll, referral, seller, amount):
    """현재 방식: 판매 시 부모를 하나씩 조회"""
    parents = {child: parent for child, parent in zip(enroll, referral)}
    incomes = defaultdict(int)

    for person, count in zip(seller, amount):
        income = count * 100
        current = person

        while current != '-' and income > 0:
            incomes[current] += income - income // 10
            income //= 10
            current = parents[current]  # 딕셔너리 조회

    return [incomes.get(person, 0) for person in enroll]


# ============================================================
# 방법 2: 전체 경로 미리 계산 (Eager)
# ============================================================
def solution_precompute_all(enroll, referral, seller, amount):
    """모든 조직원의 경로를 미리 계산"""
    parents = {child: parent for child, parent in zip(enroll, referral)}
    incomes = defaultdict(int)

    # 전처리: 모든 조직원의 경로 계산 O(N × H)
    def get_path(person):
        """루트까지의 경로 반환"""
        path = []
        current = person
        while current != '-':
            path.append(current)
            current = parents[current]
        return path

    paths = {person: get_path(person) for person in enroll}

    # 판매 처리
    for person, count in zip(seller, amount):
        income = count * 100
        path = paths[person]  # 미리 계산된 경로 사용

        for member in path:
            if income < 1:
                break
            incomes[member] += income - income // 10
            income //= 10

    return [incomes.get(person, 0) for person in enroll]


# ============================================================
# 방법 3: 지연 캐싱 (Lazy) - 판매원만 계산
# ============================================================
def solution_lazy_cache(enroll, referral, seller, amount):
    """판매가 발생한 조직원의 경로만 계산하고 캐싱"""
    parents = {child: parent for child, parent in zip(enroll, referral)}
    incomes = defaultdict(int)
    path_cache = {}  # 계산된 경로만 저장

    def get_path_cached(person):
        """경로를 계산하고 캐싱"""
        if person in path_cache:
            return path_cache[person]

        path = []
        current = person
        while current != '-':
            path.append(current)
            current = parents[current]

        path_cache[person] = path
        return path

    # 판매 처리
    for person, count in zip(seller, amount):
        income = count * 100
        path = get_path_cached(person)  # 필요할 때만 계산

        for member in path:
            if income < 1:
                break
            incomes[member] += income - income // 10
            income //= 10

    return [incomes.get(person, 0) for person in enroll]


# ============================================================
# 방법 4: 인덱스 기반 배열 (최적화)
# ============================================================
def solution_array_indexed(enroll, referral, seller, amount):
    """인덱스 기반 배열로 최적화"""
    n = len(enroll)

    # 이름 -> 인덱스 매핑
    name_to_idx = {name: i for i, name in enumerate(enroll)}
    name_to_idx['-'] = -1

    # 부모 인덱스 배열 (정수 배열이 딕셔너리보다 빠름)
    parent_idx = [name_to_idx[ref] for ref in referral]

    # 수익 배열
    incomes = [0] * n

    # 판매 처리
    for person, count in zip(seller, amount):
        income = count * 100
        current = name_to_idx[person]

        while current != -1 and income > 0:
            incomes[current] += income - income // 10
            income //= 10
            current = parent_idx[current]  # 배열 인덱스 접근

    return incomes


# ============================================================
# 성능 비교
# ============================================================
if __name__ == "__main__":
    import time
    import tracemalloc

    # 테스트 데이터
    enroll = ['john', 'mary', 'edward', 'sam', 'emily', 'jaimie', 'tod', 'young']
    referral = ['-', '-', 'mary', 'edward', 'mary', 'mary', 'jaimie', 'edward']
    seller = ['young', 'john', 'tod', 'emily', 'mary']
    amount = [12, 4, 2, 5, 10]

    methods = [
        ("딕셔너리 조회", solution_dict),
        ("전체 경로 미리 계산", solution_precompute_all),
        ("지연 캐싱", solution_lazy_cache),
        ("인덱스 배열", solution_array_indexed),
    ]

    print("=" * 70)
    print("성능 비교 (1000번 반복)")
    print("=" * 70)

    for name, func in methods:
        # 메모리 측정 시작
        tracemalloc.start()

        # 시간 측정
        start = time.perf_counter()
        for _ in range(1000):
            result = func(enroll, referral, seller, amount)
        elapsed = (time.perf_counter() - start) * 1000

        # 메모리 측정
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"\n[{name}]")
        print(f"  실행 시간: {elapsed:.2f}ms")
        print(f"  피크 메모리: {peak / 1024:.2f}KB")
        print(f"  결과: {result}")

    print("\n" + "=" * 70)
