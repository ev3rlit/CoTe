import sys

# 입력 제한 N = 10000,  순회 가능

input()
commands = map(lambda x : x.split(), sys.stdin.readlines())

def solution(commands):

    stack = []
    anwser = []

    for command_info in commands:

        cmd = command_info[0]

        if cmd == 'push':
            param = command_info[1]
            stack.append(param)

        elif cmd == 'pop':
            if stack:
                anwser.append(stack.pop())
            else:
                anwser.append(-1)

        elif cmd == 'size':
            anwser.append(len(stack))

        elif cmd == 'empty':
            anwser.append(1 if not stack else 0)

        elif cmd == 'top':
            if stack:
                anwser.append(stack[-1])
            else:
                anwser.append(-1)


    print(*anwser, sep='\n')

solution(commands)