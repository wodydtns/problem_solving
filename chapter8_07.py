from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    # 각 코스 요리 길이에 대해
    for c in course:
        menu = []
        # 모든 주문에 대해
        for order in orders:
            # combination을 이용해 가능한 메뉴 구성을 모두 구함
            comb = combinations(sorted(order), c)
            menu += comb
        # 각 메뉴 구성이 몇 번 주문되었는지 세어줌
        counter = Counter(menu)
        print(counter)
        # 가장 많이 주문된 구성이 1번 이상 주문된 경우
        if len(counter) != 0 and max(counter.values()) != 1:
            for m, cnt in counter.items():
                # 가장 많이 주문된 구성을 찾아서
                if cnt == max(counter.values()):
                    # 정답 리스트에 추가
                    answer.append("".join(m))
    return sorted(answer)


# case 1
# orders=["ABCFG","AC","CDE","ACDE","BCFG","ACDEH"]
# course = [2,3,4]
# result = ["AC","ACDE","BCFG","CDE"]

# case 2
# orders=["ABCDE","AB","CD","ADE","XYZ","XYZ","ACD"]
# course = [2,3,5]
# result = ["ACD","AD","ADE","CD","XYZ"]

# case 3
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
result = ["WX", "XY"]

solution(orders, course)
