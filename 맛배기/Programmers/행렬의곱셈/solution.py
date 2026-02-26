def solution(arr1, arr2):

    n, m = len(arr1), len(arr1[0])
    _, l = len(arr2), len(arr2[0])

    ret = [[0] * l for _ in range(n)]

    for i in range(n):
        for j in range(l):

            sum = 0
            for k in range(m) :
                sum += arr1[i][k] * arr2[k][j]
            
            ret[i][j] = sum

    return ret