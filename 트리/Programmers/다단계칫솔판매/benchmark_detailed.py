"""
다양한 시나리오에서 경로 캐싱 전략 비교
"""

from collections import defaultdict
import time
import random

# ============================================================
# 4가지 구현 방식
# ============================================================

def solution_dict(enroll, referral, seller, amount):
    """현재 방식: 딕셔너리 조회"""
    parents = {child: parent for child, parent in zip(enroll, referral)}
    incomes = defaultdict(int)

    for person, count in zip(seller, amount):
        income = count * 100
        current = person
        while current != '-' and income > 0:
            incomes[current] += income - income // 10
            income //= 10
            current = parents[current]

    return [incomes.get(person, 0) for person in enroll]


def solution_precompute_all(enroll, referral, seller, amount):
    """전체 경로 미리 계산"""
    parents = {child: parent for child, parent in zip(enroll, referral)}
    incomes = defaultdict(int)

    # 전처리
    def get_path(person):
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
        for member in paths[person]:
            if income < 1:
                break
            incomes[member] += income - income // 10
            income //= 10

    return [incomes.get(person, 0) for person in enroll]


def solution_lazy_cache(enroll, referral, seller, amount):
    """지연 캐싱 - 판매원만"""
    parents = {child: parent for child, parent in zip(enroll, referral)}
    incomes = defaultdict(int)
    path_cache = {}

    def get_path(person):
        if person in path_cache:
            return path_cache[person]

        path = []
        current = person
        while current != '-':
            path.append(current)
            current = parents[current]

        path_cache[person] = path
        return path

    for person, count in zip(seller, amount):
        income = count * 100
        for member in get_path(person):
            if income < 1:
                break
            incomes[member] += income - income // 10
            income //= 10

    return [incomes.get(person, 0) for person in enroll]


def solution_array(enroll, referral, seller, amount):
    """인덱스 배열"""
    n = len(enroll)
    name_to_idx = {name: i for i, name in enumerate(enroll)}
    name_to_idx['-'] = -1

    parent_idx = [name_to_idx[ref] for ref in referral]
    incomes = [0] * n

    for person, count in zip(seller, amount):
        income = count * 100
        current = name_to_idx[person]

        while current != -1 and income > 0:
            incomes[current] += income - income // 10
            income //= 10
            current = parent_idx[current]

    return incomes


# ============================================================
# 테스트 데이터 생성기
# ============================================================

def generate_test_data(n_members, tree_depth, n_sales, duplicate_rate=0.0):
    """
    테스트 데이터 생성

    Args:
        n_members: 조직원 수
        tree_depth: 트리 평균 깊이
        n_sales: 판매 건수
        duplicate_rate: 같은 판매원의 중복 판매 비율 (0.0 ~ 1.0)
    """
    enroll = [f'member_{i}' for i in range(n_members)]
    referral = ['-']

    # 트리 구조 생성 (깊이 제어)
    for i in range(1, n_members):
        # 깊이를 제어하기 위해 최근 멤버 중에서 부모 선택
        parent_range = max(1, i - tree_depth)
        parent_idx = random.randint(0, i - 1) if i > parent_range else random.randint(0, max(0, i - 1))
        referral.append(enroll[parent_idx])

    # 판매 데이터 생성
    if duplicate_rate == 0.0:
        # 중복 없음: 랜덤하게 선택
        seller = [random.choice(enroll) for _ in range(n_sales)]
    else:
        # 중복 있음: 일부 판매원이 여러 번 판매
        n_unique = int(n_sales * (1 - duplicate_rate))
        unique_sellers = random.sample(enroll, min(n_unique, n_members))
        seller = []
        for _ in range(n_sales):
            if random.random() < duplicate_rate and seller:
                # 이미 판매한 사람 다시 선택
                seller.append(random.choice(seller))
            else:
                seller.append(random.choice(unique_sellers))

    amount = [random.randint(1, 10) for _ in range(n_sales)]

    return enroll, referral, seller, amount


# ============================================================
# 벤치마크
# ============================================================

def benchmark(name, enroll, referral, seller, amount, repeat=100):
    """벤치마크 실행"""
    methods = [
        ("딕셔너리", solution_dict),
        ("전체 경로", solution_precompute_all),
        ("지연 캐싱", solution_lazy_cache),
        ("인덱스 배열", solution_array),
    ]

    print(f"\n{'='*70}")
    print(f"테스트: {name}")
    print(f"  조직원: {len(enroll)}명, 판매: {len(seller)}건")
    print(f"  평균 깊이: ~{len(enroll) // max(sum(1 for r in referral if r == '-'), 1)}")
    print(f"{'='*70}")

    results = []
    for method_name, func in methods:
        start = time.perf_counter()
        for _ in range(repeat):
            result = func(enroll, referral, seller, amount)
        elapsed = (time.perf_counter() - start) * 1000 / repeat

        results.append((method_name, elapsed))
        print(f"{method_name:12s}: {elapsed:6.3f}ms")

    # 가장 빠른 것 표시
    fastest = min(results, key=lambda x: x[1])
    print(f"\n⭐ 최고 성능: {fastest[0]} ({fastest[1]:.3f}ms)")

    return results


if __name__ == "__main__":
    print("\n" + "="*70)
    print(" 경로 캐싱 전략 성능 비교")
    print("="*70)

    # 시나리오 1: 작은 데이터, 중복 없음 (프로그래머스 예제)
    enroll = ['john', 'mary', 'edward', 'sam', 'emily', 'jaimie', 'tod', 'young']
    referral = ['-', '-', 'mary', 'edward', 'mary', 'mary', 'jaimie', 'edward']
    seller = ['young', 'john', 'tod', 'emily', 'mary']
    amount = [12, 4, 2, 5, 10]
    benchmark("시나리오 1: 작은 데이터 (중복 없음)", enroll, referral, seller, amount, repeat=1000)

    # 시나리오 2: 중간 데이터, 중복 없음
    enroll, referral, seller, amount = generate_test_data(
        n_members=100, tree_depth=5, n_sales=50, duplicate_rate=0.0
    )
    benchmark("시나리오 2: 중간 데이터 (중복 없음)", enroll, referral, seller, amount, repeat=100)

    # 시나리오 3: 중간 데이터, 중복 많음 (70%)
    enroll, referral, seller, amount = generate_test_data(
        n_members=100, tree_depth=5, n_sales=200, duplicate_rate=0.7
    )
    benchmark("시나리오 3: 중간 데이터 (중복 70%)", enroll, referral, seller, amount, repeat=100)

    # 시나리오 4: 큰 데이터, 중복 없음
    enroll, referral, seller, amount = generate_test_data(
        n_members=1000, tree_depth=10, n_sales=500, duplicate_rate=0.0
    )
    benchmark("시나리오 4: 큰 데이터 (중복 없음)", enroll, referral, seller, amount, repeat=10)

    # 시나리오 5: 큰 데이터, 중복 많음 (80%)
    enroll, referral, seller, amount = generate_test_data(
        n_members=1000, tree_depth=10, n_sales=2000, duplicate_rate=0.8
    )
    benchmark("시나리오 5: 큰 데이터 (중복 80%)", enroll, referral, seller, amount, repeat=10)

    # 시나리오 6: 깊은 트리
    enroll, referral, seller, amount = generate_test_data(
        n_members=500, tree_depth=50, n_sales=200, duplicate_rate=0.5
    )
    benchmark("시나리오 6: 깊은 트리 (깊이~50)", enroll, referral, seller, amount, repeat=10)

    print("\n" + "="*70)
    print("벤치마크 완료")
    print("="*70)
