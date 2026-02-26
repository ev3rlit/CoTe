def solution(cards1, cards2, goal):

    # goal를 순회
    # cards1 혹은 cards2의 현재 단어를 비교
    # 둘중에 사용 가능한 카드가 있으면  해당 카드 인덱스 증가
    # 둘중에 아무것도 사용 가능한 카드가 없으면 실패

    c1idx = 0
    c2idx = 0

    for want in goal:
        if len(cards1) > c1idx and cards1[c1idx] == want:
            c1idx += 1
        elif len(cards2) > c2idx and cards2[c2idx] == want:
            c2idx += 1
        else:
            return 'No'

    return 'Yes'

# 카드 덱이 N개 있다고 할 때 좀더 범용적인 코드
def solutionv2(decks, goal):
    next_card_indices = {i:0 for i in range(len(decks))}

    for want in goal:
        found = False
        for deck_idx in range(len(decks)):
            card_idx = next_card_indices[deck_idx]
            if len(decks[deck_idx]) > card_idx and decks[deck_idx][card_idx] == want:
                next_card_indices[deck_idx] += 1
                found = True
                break
        if not found:
            return 'No'
    return 'Yes'

# 카드 덱이 2개 이상인 상황에 특화된 코드
def solutionv3(cards1, cards2, goal):
    decks = [cards1, cards2]
    for want in goal:

        found = False
        for card_deck in decks:
            if card_deck and card_deck[0] == want:
                card_deck.pop(0)
                found = True
                break

        if not found:
            return 'No'

    return 'Yes'

# 큐 자료구조를 활용한 풀이
def solutionv4(cards1, cards2, goal):
    from collections import deque

    deck1 = deque(cards1)
    deck2 = deque(cards2)

    for want in goal:
        if deck1 and deck1[0] == want:
            deck1.popleft()
        elif deck2 and deck2[0] == want:
            deck2.popleft()
        else:
            return 'No'

    return 'Yes'
