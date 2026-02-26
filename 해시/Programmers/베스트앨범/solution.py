# 각 장르별 전체 플레이 횟수를 기준으로 정렬
# 장르내에서 최대 2개의 노래만 선별하며,  재생횟수 내림차순

from collections import defaultdict

def solution(genres, plays):

    answers = []


    # 각 장르별 총 플레이 횟수를 집계
    # 각 장르별 노래 플레이 횟수 집계
    # 노래의 플레이 횟수는 내림차순, 노래 번호 오름차순
    # 장르를 내림차순 정렬
    # 정렬된 장르를 순회하면서 2개를 픽하여 저장

    genre_plays = defaultdict(int)
    for (genre, play) in zip(genres, plays):
        genre_plays[genre] += play

    # key : genre, value : [(music_id, plays)]
    genre_music = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_music[genre].append((i,play))

    # 배열 정렬
    for genre in genre_music:
        genre_music[genre].sort(key = lambda x : (-x[1], x[0]))
    
    top_genres = sorted(genre_plays.items(), key = lambda x : x[1], reverse=True)
    for genre, _ in top_genres:
        # 노래 번호를 추가
        answers.extend([x[0] for x in genre_music[genre][:2]])

    return answers
    