def solution(decimal):

    stack = []
    while decimal > 0:
        remainder = decimal % 2
        stack.append(remainder)
        decimal //= 2
    
    binary = ""
    while stack:
        binary += str(stack.pop())
    return binary
    