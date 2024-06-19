def polynomial_hash(str):
    # 소수
    p = 31
    # 버킷 크기
    m = 1_000_000_007
    hash_value = 0
    for char in str:
        hash_value = (hash_value * p + ord(char)) % m
    return hash_value


def solution(string_list, query_list):
    # string_list의 각 문자열에 대해 다항 해시값을 계산
    hash_list = [polynomial_hash(str) for str in string_list]

    # query_list의 각 문자열이 string_list에 있는지 확인
    result = []
    for query in query_list:
        query_hash = polynomial_hash(query)
        if query_hash in hash_list:
            result.append(True)
        else:
            result.append(False)
    return result


string_list = ["apple", "banana", "cherry"]
query_list = ["banana", "kiwi", "melon", "apple"]
solution(string_list, query_list)
