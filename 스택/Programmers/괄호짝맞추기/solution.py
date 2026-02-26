def solution(s):

    # 열린 괄호 수 카운트
    opens = 0

    for char in s:
        # 조기 종료 조건
        # 0인데 닫는 괄호는 짝이 안맞음
        if opens == 0 and char == ')':
            return False

        if char == '(':
            opens += 1
        elif char == ')':
            opens -= 1

    # 최근 열린 괄호가 없으면 짝
    return opens == 0    