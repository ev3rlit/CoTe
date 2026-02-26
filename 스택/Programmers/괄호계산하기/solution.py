
# 문자열을 왼쪽으로 회전하기 (회전할 횟수 계산)
# 0번 부터 문자열 길이 -1 까지 회전 진행
# 회전된 상태에서 괄호짝이 맞는지 확인
# 각 문자마다 열린 괄호 수 카운트
# 닫힌 괄호가 더 많아지면 조기 종료

# 괄호 배열이 짝이 맞는지 확인합니다.
def validate(s) -> bool:
    mapping = {')' : '(', ']' : '[', '}' : '{'}
    opens = set(['(', '{', '['])
    stack = []

    for char in s:
        if char in opens:
            stack.append(char)
            continue

        if len(stack) == 0:
            return False

        popped = stack.pop()
        found = mapping.get(char)

        if found != popped:
            return False
    
    return len(stack) == 0



def validate2(s, offset) -> bool:
    mapping = {')' : '(', ']' : '[', '}' : '{'}
    opens = set(mapping.values())
    stack = []

    for i in range(len(s)):
        char = s[(i + offset) % len(s)]
        if char in opens:
            stack.append(char)
            continue
        
        if len(stack) == 0:
            return False
        
        if stack.pop() != mapping.get(char):
            return False
    
    return len(stack) == 0

def solution(s):
    return sum(validate(s[i:] + s[:i]) for i in range(len(s)))

def solutionv2(s):
    return sum(validate2(s, i) for i in range(len(s)))



                




    