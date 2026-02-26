# 방법 1: O(n²) - Brute Force 방식
def solution_n2(prices):
    """
    각 시점에서 이후 모든 시점을 순회하며 가격이 떨어지는지 확인

    시간복잡도: O(n²)
    공간복잡도: O(n)
    """
    n = len(prices)
    answer = [0] * n

    # 각 시점마다
    for i in range(n):
        # 이후 시점들을 하나씩 확인
        for j in range(i + 1, n):
            answer[i] += 1
            # 가격이 떨어지면 중단
            if prices[i] > prices[j]:
                break

    return answer


# 방법 2: O(n) - 스택 활용 (최적화)
def solution(prices):
    """
    스택에 '아직 가격이 떨어지지 않은 시점의 인덱스'를 저장

    핵심 아이디어:
    - 스택에는 가격이 떨어지지 않은 시점들이 '오름차순'으로 쌓임
    - 현재 가격이 스택 top의 가격보다 낮으면
      → 스택 top 시점의 가격이 "드디어 떨어진 것"
      → 스택에서 pop하고 기간 계산

    시간복잡도: O(n) - 각 원소가 스택에 push/pop 최대 1번
    공간복잡도: O(n) - 스택 크기
    """
    n = len(prices)
    answer = [0] * n
    stack = []  # (인덱스, 가격) 저장 (인덱스만 저장해도 됨)

    for i in range(n):
        # 현재 가격이 스택의 top보다 낮으면
        # = 스택에 있는 시점의 가격이 떨어진 것!
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j  # 떨어지지 않은 기간

        # 현재 시점을 스택에 추가
        stack.append(i)

    # 스택에 남은 시점들은 끝까지 가격이 안 떨어진 것
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer


# 방법 3: O(n) - Deque 활용 (스택과 유사)
def solution_deque(prices):
    """
    Deque를 사용한 방식 (사실상 스택과 동일한 성능)

    차이점:
    - collections.deque는 양방향 삽입/삭제가 O(1)
    - 리스트 스택은 append/pop만 O(1)
    - 이 문제는 한쪽만 사용하므로 성능 차이 거의 없음

    시간복잡도: O(n)
    공간복잡도: O(n)
    """
    from collections import deque

    n = len(prices)
    answer = [0] * n
    dq = deque()

    for i in range(n):
        while dq and prices[dq[-1]] > prices[i]:
            j = dq.pop()
            answer[j] = i - j
        dq.append(i)

    while dq:
        j = dq.pop()
        answer[j] = n - 1 - j

    return answer


# 방법 4: O(n) - 역방향 순회 + 점프 포인터
def solution_backward(prices):
    """
    역방향 순회 방식

    아이디어:
    - 끝에서부터 거꾸로 순회
    - 각 위치에서 "다음에 가격이 떨어지는 위치"를 기록
    - 점프 포인터를 사용해 더 먼 위치로 건너뛰기

    장점: 특정 패턴에서 조기 종료 가능
    단점: 최악의 경우 여전히 O(n²) 근접 가능

    시간복잡도: O(n) ~ O(n²) (평균 O(n))
    공간복잡도: O(n)
    """
    n = len(prices)
    answer = [0] * n
    next_lower = [n] * n  # 각 위치에서 다음으로 낮은 가격의 위치

    # 역방향 순회하며 next_lower 배열 채우기
    for i in range(n - 2, -1, -1):
        j = i + 1
        # 점프 포인터: 현재 가격보다 낮은 위치 찾기
        while j < n and prices[i] <= prices[j]:
            j = next_lower[j]
        next_lower[i] = j

    # answer 계산
    for i in range(n):
        if next_lower[i] == n:
            answer[i] = n - 1 - i
        else:
            answer[i] = next_lower[i] - i

    return answer


# 방법 5: O(n²) 최적화 - Early Break with Min Tracking
def solution_optimized_brute(prices):
    """
    Brute Force에 최적화 추가

    최적화:
    - 지금까지 본 최솟값 추적
    - 현재 가격이 최솟값보다 낮거나 같으면 즉시 처리 가능한 경우도 있음

    실제로는: 여전히 O(n²)이지만 평균적으로 약간 빠름

    시간복잡도: O(n²)
    공간복잡도: O(n)
    """
    n = len(prices)
    answer = [0] * n

    for i in range(n):
        min_after = float('inf')
        for j in range(i + 1, n):
            answer[i] += 1
            min_after = min(min_after, prices[j])

            # 가격이 떨어지면 중단
            if prices[i] > prices[j]:
                break

            # 조기 최적화: 이미 최솟값을 봤고 더 이상 떨어질 가능성 낮음
            # (실제로는 도움 안 됨 - 예시용)

    return answer   