def solution(board, moves):
    boomed = 0

    # 보드의  열을 각각 스택으로 저장
    # moves 배열 순회
    # 각 이동 위치에서 가장 위에 있는 인형과 현재 바구니와 비교합니다.
    # 동일하면  boom!!  증가
    # 그렇지 않으면 스택에 저장 (사실 여기서 최근 것 1개와 비교하므로 굳이 스택일 필요는없음)

    rows = len(board)
    cols = len(board[0])
    dolls = [[],]

    for c in range(cols):
        line = []
        for r in range(rows-1, -1, -1):  # 0번째 행까지 포함
            if board[r][c] != 0:
                line.append(board[r][c])
        dolls.append(line)  


    basket = []
    for m in moves:
        # 해당 위치에 인형이 없으면 다음으로
        if not dolls[m]:
            continue

        # # 바스켓이 비어있ㅇ면 넣기
        # if not basket:
        #     basket.append(dolls[m][-1])
        #     dolls[m].pop()
        #     continue
        
        # 바스켓의 최상단에 있는것과 인형이 동일하면 boom!
        # 바스켓에 있는 인형은 pop
        if basket and dolls[m][-1] == basket[-1]:
            boomed += 2
            basket.pop()
            dolls[m].pop()
        # 다르면 인형만 넣기
        else:
            basket.append(dolls[m].pop())


    return boomed
    