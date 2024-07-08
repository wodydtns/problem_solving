def dfs(cur_k, cnt, dungeons, visited):
    answer_max = cnt
    for i in range(len(dungeons)):
        # 현재 피로도(cur_k)가 i번째 던전의 최소 필요 피로도보다 크거나 같고
        # i번째 던전을 방문한 적이 없다면
        if cur_k >= dungeons[i][0] and visited[i] == 0:
            # i번째 던전을 방문 처리
            visited[i] = 1

            # 현재까지의 최대 탐험 가능 던전수와 i번째 던전에서 이동할 수 있는 최대 탐험
            # 가능 던전 수 중 큰 값을 선택해 업데이트
            answer_max = max(
                answer_max, dfs(cur_k - dungeons[i][1], cnt + 1, dungeons, visited)
            )
            visited[i] = 0
    return answer_max


def solution(k, dungeons):
    # 던전 방문 여부를 저장할 지역 배열
    visited = [0] * len(dungeons)
    answer_max = dfs(k, 0, dungeons, visited)
    return answer_max


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
