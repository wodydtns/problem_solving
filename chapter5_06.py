def solution(n, stages):
    # 스테이지별 도전자 수를 구함
    challenger = [0] * (n + 2)
    for stage in stages:
        challenger[stage] += 1
    print(challenger)

    # 스테이지별 실패한 사용자 수 계산
    fails = {}
    total = len(stages)

    # 각 스테이지를 순회하며, 실패율 계산
    for i in range(1, n + 1):
        # 도전한 사람이 없는 경우
        if challenger[i] == 0:
            fails[i] = 0
        else:
            # 실패율 구함
            fails[i] = challenger[i] / total
            # 다음 스테이지 실패율을 구하기 위해 현재 스테이지의 인원을 뺌
            total -= challenger[i]

    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    return result


n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(n, stages)
