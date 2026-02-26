from functools import lru_cache

class Solution:

    def with_bottomup(self, word1: str, word2: str) -> int:

        # ptr1, ptr2 저장을 위한 캐시 테이블
        dp = [[len(word1)+len(word2)] * (len(word2)+1) for _ in range(len(word1)+1)]

        for ptr1 in range(len(word1)):
            dp[ptr1][len(word2)] = len(word1) - ptr1

        for ptr2 in range(len(word2)):
            dp[len(word1)][ptr2] = len(word2) - ptr2

        dp[len(word1)][len(word2)] = 0

        # 행은 word1, 열은 word2로 순회
        for ptr1 in reversed(range(len(word1))):
            for ptr2 in reversed(range(len(word2))):
                min_edit_distance = len(word1) + len(word2)

                # 동일한 경우
                if word1[ptr1] == word2[ptr2]:
                    min_edit_distance = min(min_edit_distance, dp[ptr1 + 1][ptr2 + 1])
                    dp[ptr1][ptr2] = min_edit_distance

                # 삽입
                min_edit_distance = min(min_edit_distance, dp[ptr1][ptr2+1] + 1)

                # 삭제
                min_edit_distance = min(min_edit_distance, dp[ptr1+1][ptr2] + 1)

                # 교체
                min_edit_distance = min(min_edit_distance, dp[ptr1+1][ptr2+1] + 1)

                dp[ptr1][ptr2] = min_edit_distance

        return dp[0][0]

    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(None)
        def dp(ptr1, ptr2):
            # 기저 조건
            # ptr1이 word1의 길이를 초과하는 경우
            # word2의 나머지에 맞춰서 word1에 삽입
            if ptr1 == len(word1):
                return len(word2) - ptr2            
            # ptr2가 word2의 길이를 초과하는 경우
            # word2와 동일하게 맞추기 위해 word1의 일부를 삭제
            if ptr2 == len(word2):
                return len(word1) - ptr1
            
            min_edit_distance = len(word1) + len(word2)

            # 동일한 경우
            if word1[ptr1] == word2[ptr2]:
                # 별도의 횟수 증가 없이 두 단어 모두 다음 포인터로 이동
                min_edit_distance = min(min_edit_distance, dp(ptr1+1, ptr2+1))

            # 삽입
            # word1의 현재 포인터 앞쪽에 추가해야 word2의 ptr2의 문자와 동일함.
            # 이것이 최소 삽입가능한 방법
            min_edit_distance = min(min_edit_distance, dp(ptr1, ptr2+1) + 1)

            # 삭제
            # 삭제는 별다른 선택지가 없음. word1의 일부 문자를 지우고 그다음으로 가야함.
            min_edit_distance = min(min_edit_distance, dp(ptr1+1, ptr2) + 1)

            # 교체
            # 교체의 최소는 word1와 word2각각의 위치에서 동일한 문제로 바꾸는것임.
            min_edit_distance = min(min_edit_distance, dp(ptr1+1, ptr2+1) + 1)

            return min_edit_distance
        
        return dp(0,0)