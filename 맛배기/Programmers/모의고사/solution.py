def solution(answers):

    # 수포자 번호 : 점수 형태로  각 수포자들의 점수를 기록해야함
    # 만약 수포자 패턴보다 답안의 길이가 작으면?
    # 수포자 패턴보다 답안의 길이가 길다면?
    # 나머지 연산을 이용하면  답안의 길이와 패턴의 길이가 달라도 순차적으로가능함


    # 문제의 정답과 수포자 패턴의 답이 동일하면  점수 증가

    # 최고점이 동일한 사람을 반환

    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5],
    ]

    scores = {1 : 0, 2 : 0, 3 : 0}


    # 답안을 순회하면서
    for i, answer in enumerate(answers) :

        # 각 수포자들의 답안 패턴을 선택
        # 각 수포자들의 답안 패턴 범위를 넘지않도록 나머지 연산 순회
        for j, pattern in enumerate(patterns) :
            expected = pattern[i % len(pattern)]

            if answer == expected :
                scores[j+1] += 1
            
    # 수포자들중 최고점을 기록한 사람의 점수 찾기
    max_score = 0
    for _, score in scores.items():
        if max_score < score :
            max_score = score
    
    # 최고점이 동일한 사람 기록
    result = []
    for i, score in scores.items():
        if max_score == score:
            result.append(i)

    return result
    
def simpler_solution(answers):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5],
    ]

    scores = {1 : 0, 2 : 0, 3 : 0}

    for i, answer in enumerate(answers) :
        for j, pattern in enumerate(patterns) :
            if answer == pattern[i % len(pattern)] :
                scores[j+1] += 1
            
    max_score = max(scores.values())
    
    result = [i for i, score in scores.items() if score == max_score]

    return result