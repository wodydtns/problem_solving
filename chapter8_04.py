def solution(want, number, discount):
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    answer = 0

    # 특정일 i에 회원가입 시 할인받을 수 있는 품목 체크
    for i in range(len(discount) - 9):
        # i일 회원가입 시 할인받는 제품 및 개수를 담을 딕셔너리
        discount_10d = {}

        for j in range(i, i + 10):
            if discount[j] in want_dict:
                discount_10d[discount[j]] = discount_10d.get(discount[j], 0) + 1
        # 할인하는 상품의 개수가 원하는 수량과 일차하면 정답 변수 1에 추가
        if discount_10d == want_dict:
            answer += 1
    return answer


# case 1
"""
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = [
    "chicken",
    "apple",
    "apple",
    "banana",
    "rice",
    "apple",
    "pork",
    "banana",
    "pork",
    "rice",
    "pot",
    "banana",
    "apple",
    "banana",
]
"""
want = ["apple"]
number = [10]
discount = [
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
    "banana",
]
solution(want, number, discount)
