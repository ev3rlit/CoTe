def hash_string(s):
    p = 31
    m = 1_000_000_007
    hash_value = 0

    for char in s:
        hash_value = (hash_value * p + ord(char)) % m
    return hash_value

def solution(string_list, query_list):
    hash_list = [hash_string(s) for s in string_list]
    result = []

    for query in query_list:
        query_hash = hash_string(query)
        if query_hash in hash_list:
            result.append(True)
        else:
            result.append(False)

    return result