import string


def solution(msg):

    dictionary = { chr(i+65) : i+1 for i in range(0,26)}
    idx = 26

    # 입력 크기가 1000 이하 이므로 N^2도 가능해보임
    # 출력 길이는 N임

    # 순회하면서 사전에 등록된 글자중 가장긴 길이

    # KAKAO
    # KAKAO, KAKA, KAK, KA, K
    # 긴순서대로 순회하면서 사전 탐색하면 가장 긴 문자열 찾을 수 있음
    # 찾으면 사전에 검색된 번호를 출력에 저장
    # 다음 글자 위치를 찾고

    i = 0
    answer = []
    while i < len(msg):

        # 현재 위치에서 가장 긴 길이 문자를 찾아야함
        # 뒤에서 부터 가장 긴 길이 문자를 탐색
        for j in range(len(msg),i,-1):
            if msg[i:j] not in dictionary:
                continue

            # 출력에 현재 입력의 색인 번호 저장
            answer.append(dictionary[msg[i:j]])

            # 다음 글자가 있다면 사전에 추가
            if j < len(msg):
                idx += 1
                dictionary[msg[i:j+1]] = idx

            # 입력에서 w를 제거 하는 대신 위치를 옮기기
            i = j
            break

    return answer


def solutionv2(msg):
    """
    LZW 압축 알고리즘 개선 버전

    개선 사항:
    1. string.ascii_uppercase 사용 (하드코딩 제거)
    2. 앞에서부터 확장하는 방식으로 O(N) 최적화
    3. 변수명 개선 (idx → dict_size, i → pos)

    시간 복잡도: O(N)
    공간 복잡도: O(N)
    """
    # A-Z 초기화 (하드코딩 없음!)
    dictionary = {char: idx for idx, char in enumerate(string.ascii_uppercase, start=1)}
    dict_size = len(dictionary)

    pos = 0
    answer = []

    while pos < len(msg):
        # 현재 위치에서 한 글자부터 시작
        w = msg[pos]

        # 사전에 있는 동안 계속 확장
        while pos + len(w) < len(msg) and w + msg[pos + len(w)] in dictionary:
            w += msg[pos + len(w)]

        # 출력에 색인 번호 추가
        answer.append(dictionary[w])

        # 다음 글자를 포함한 문자열을 사전에 추가
        if pos + len(w) < len(msg):
            dict_size += 1
            dictionary[w + msg[pos + len(w)]] = dict_size

        # 다음 위치로 이동
        pos += len(w)

    return answer