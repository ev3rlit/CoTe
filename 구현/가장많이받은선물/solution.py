# 1. Friend 객체 생성
# - name : 이름, 
# - given : 준 횟수
# - received : 받은 횟수
# - gift_to : 특정 친구에게 선물준 횟수
# - expected : 다음달 받을 횟수
# 1. 기본값 초기화
# - zero value로 Friend  dict 생성
# - gift_to는 defaultdict이용
# 2. Gift를 순회하면서 Friend의 내용을 채워 넣기.
# - giver_name, receiver_name을 토대로 friend_map에 채워넣기
# - giver의 given += 1,  receiver의 received += 1
# - giver의 gift_to[receiver_name] += 1
# 3. friend 2중 반복을 통해 모든 친구들끼리 비교
# - for i in range(len(friend)):
#   - for j in range(i,len(friend))
# 둘이 선물 준 횟수를 비교하여 더 많이준 사람이 선물 받음
# 둘이 서로 선물 주고 받은 기록이 없다면 선물지수 계산
# 선물지수 마져 동일하면 무시

from collections import defaultdict

class Friend:
    def __init__(self, name):
        self.name = name
        self.given = 0
        self.received = 0
        self.gift_to = defaultdict(int)
        self.expected = 0

def solution(friends, gifts):
    
    # 1. 기본값 초기화
    friend_map = {name : Friend(name) for name in friends}
    
    # 2. 기프트 순회
    for gift in gifts:
        giver_name, receiver_name = gift.split()
        
        giver = friend_map[giver_name]
        receiver = friend_map[receiver_name]
        
        giver.given += 1
        giver.gift_to[receiver_name] += 1
        receiver.received += 1
        
    # 3. 친구들끼리 서로 비교
    for i in range(len(friend_map)):
        for j in range(i+1, len(friend_map)):
            
            a = friend_map[friends[i]]
            b = friend_map[friends[j]]
            
            a_to_b = a.gift_to[b.name]
            b_to_a = b.gift_to[a.name]

            # 둘이 선물 준 횟수를 비교하여 더 많이준 사람이 선물 받음
            if a_to_b > b_to_a:
                a.expected += 1
            elif b_to_a > a_to_b:
                b.expected += 1
            else:
            # 둘이 서로 선물 주고 받은 기록이 없다면 선물지수 계산
                a_score = a.given - a.received
                b_score = b.given - b.received
                
                if a_score > b_score:
                    a.expected += 1
                elif b_score > a_score:
                    b.expected += 1
            # 선물지수 마져 동일하면 무시
    
    return max(f.expected for f in friend_map.values())
    