# 모든 문제에 대해서 각 수포자별로 패턴대로 정답 책정
# 수포자들의 점수를 초기화
# 모든 문제를 순회
# 각 수포자들의 패턴을 모듈러 연산을 이용해서 패턴 순회
# i % len(pattern) 
# 정답과 비교하여 각 수포자들의 점수를 계산
# 가장 높은 점수를 받은 수포자들을 결과 리스트에 추가
# 결과 리스트를 오름차순으로 정렬하여 반환

def solution(answers):

    patterns = [
        [1,2,3,4,5,],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5],
    ]

    scores = [0,0,0]
    
    for i, answer in enumerate(answers):
        for j in range(len(patterns)):
            if answer == patterns[j][i % len(patterns[j])]:
                scores[j] += 1
            
    max_score = max(scores)

    # 참여자 순서대로 하면 알아서 오름차순 배치
    max_participants = [ i+1 for i, score in enumerate(scores) if score == max_score]
    
    return max_participants
        