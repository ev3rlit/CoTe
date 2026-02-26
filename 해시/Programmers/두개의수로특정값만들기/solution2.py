def solution(arr, target):

    hash = [0] * (target + 1)

    for num in arr:
        if num <= target:
            hash[num] = 1

    for num in arr:

        if num >= target:
            continue

        if (target - num) == num:
            continue

        if hash[target-num]:
            return True
        
    return False

