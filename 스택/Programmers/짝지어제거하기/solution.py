def solution(s):

    # 문자를 이어 붙힌다는 개념을  스택으로  가장 최근 데이터와 현재 데이터가 동일하면
    # 제거.

    stack = []
    for char in s:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()
            continue

        # 새로운 문자라면 stack에 추가.
        stack.append(char)

    # 최종 스택이 비어있다면 모두 제거된 것.
    return int(not stack)
    