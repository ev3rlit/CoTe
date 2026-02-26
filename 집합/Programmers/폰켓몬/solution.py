def solution(nums):

    uniques = set(nums)
    n = len(nums)
    k = n // 2

    return min(k, len(uniques))