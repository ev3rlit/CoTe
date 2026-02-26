# 표 편집

#스택 #구현 #연결리스트

## 풀이 과정

### 핵심 아이디어
- 배열 기반 연결 리스트로 O(1) 삭제/복구 구현
- `up[i]`와 `down[i]` 배열로 각 행의 위/아래 행 번호 저장
- 삭제 시 연결만 바꾸고, 복구 시 연결만 복원 (실제 데이터 이동 없음)
- 삭제된 행은 스택에 저장하여 LIFO 복구 가능

### 접근 방법

1. **초기 연결 상태 설정**
   - `up[i] = i-1`: i번 행 위의 행 번호 (-1은 없음)
   - `down[i] = i+1`: i번 행 아래의 행 번호 (n은 없음)

2. **이동 (U/D 명령)**
   - X칸 이동: `up` 또는 `down` 배열을 X번 참조
   - 삭제된 행은 자동으로 건너뛰어짐 (연결이 끊어져있음)

3. **삭제 (C 명령)**
   - 현재 행을 스택에 저장
   - 위쪽 행과 아래쪽 행을 직접 연결 (현재 행 건너뛰기)
   - 커서는 아래 행으로 이동 (없으면 위 행으로)

4. **복구 (Z 명령)**
   - 스택에서 가장 최근 삭제된 행 번호 가져오기
   - 해당 행의 `up`/`down` 값으로 양쪽 연결 복원

5. **결과 생성**
   - 최종적으로 스택에 남아있는 행들이 삭제된 상태
   - O부터 n-1까지 순회하며 "O" 또는 "X" 문자열 생성

### 코드

```python
def solution(n, k, cmd):
    """
    배열 기반 연결 리스트 방식
    - up[i]: i번 행 위의 살아있는 행 (-1이면 없음)
    - down[i]: i번 행 아래의 살아있는 행 (n이면 없음)
    - 삭제 시 연결만 바꿔주면 O(1)
    """
    # 초기 연결 상태 설정
    up = [i - 1 for i in range(n)]      # up[0] = -1, up[1] = 0, ...
    down = [i + 1 for i in range(n)]    # down[0] = 1, down[1] = 2, ..., down[n-1] = n

    deleted_stack = []  # 삭제 이력 (복구용)
    current = k         # 현재 선택된 행

    for command in cmd:
        if command.startswith("D"):
            # 아래로 X칸 이동
            x = int(command.split()[1])
            for _ in range(x):
                current = down[current]

        elif command.startswith("U"):
            # 위로 X칸 이동
            x = int(command.split()[1])
            for _ in range(x):
                current = up[current]

        elif command == "C":
            # 현재 행 삭제
            deleted_stack.append(current)

            prev_row = up[current]    # 위쪽 행
            next_row = down[current]  # 아래쪽 행

            # 연결 끊기: 위쪽 행과 아래쪽 행을 직접 연결
            if prev_row != -1:
                down[prev_row] = next_row
            if next_row != n:
                up[next_row] = prev_row

            # 커서 이동: 아래 행이 있으면 아래로, 없으면 위로
            if next_row != n:
                current = next_row
            else:
                current = prev_row

        elif command == "Z":
            # 가장 최근 삭제 복구
            restored = deleted_stack.pop()
            prev_row = up[restored]    # 복구할 행의 원래 위쪽 행
            next_row = down[restored]  # 복구할 행의 원래 아래쪽 행

            # 연결 복구
            if prev_row != -1:
                down[prev_row] = restored
            if next_row != n:
                up[next_row] = restored

    # 결과 생성: 최종적으로 스택에 남아있는 것들이 삭제된 행
    result = ["O"] * n
    for row in deleted_stack:
        result[row] = "X"

    return "".join(result)
```

## 회고

### 배운 점
- 배열 기반 연결 리스트를 활용하여 삭제 및 복구를 O(1)로 구현할 수 있다는 점을 배웠다.

### 어려웠던 부분
- 단순 set으로 삭제된 행을 관리하면  시간 복잡도가 증가해버린다.  최악의 경우 O(M × N)이 될 수 있다.
- 따라서 배열 기반 연결 리스트로 삭제/복구를 O(1)로 구현하는 방법을 고민해야 했다.

### 개선할 점
- 인덱스 기반 접근 및 구현력이 부족했다. 자료구조에 대한 이해와 구현 연습이 더 필요하다.

---
**복잡도**: 시간 O(M × X_avg), 공간 O(N) - M은 명령 수, X_avg는 평균 이동 거리, N은 행 개수
**풀이 날짜**: 2025-11-03
