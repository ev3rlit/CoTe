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
