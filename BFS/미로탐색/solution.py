import sys
input = sys.stdin.readline

def solve():
    # 입력 받기
    n = int(input())
    arr = list(map(int, input().split()))

    # 풀이 로직
    arr.sort()

    # 출력
    print(*arr)

if __name__ == "__main__":
    solve()
