def solution(arr):

    result = set()

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            result.add(arr[i] + arr[j])
    
    return sorted(list(result))
    