from typing import List
from functools import lru_cache

class Solution:

    def with_botoomup(self, nums: List[int]) -> int:

        dp = [1] * len(nums)+1

        for pos in reversed(range(len(nums))):
            max_length = 1

            for next_pos  in range(pos+1, len(nums)):
                if nums[pos] < nums[next_pos]:
                    max_length = max(max_length, dp[next_pos]+1)
            
            dp[pos] = max_length
        
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(pos):
            max_length = 1
            for next_pos in range(pos+1, len(nums)):
                if nums[pos] < nums[next_pos]:
                    max_length = max(max_length, dp(next_pos) + 1)
                
            return max_length
        
        return max(dp(pos) for pos in range(len(nums)))