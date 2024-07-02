# 너비 우선 탐색 순회
from collections import defaultdict, deque


def solution(graph, start):
    # 그래프를 인접 리스트로 변환
    adj_list = defaultdict(list)

    for u, v in graph:
        adj_list[u].append(v)

    # BFS 탐색 함수
    def bfs(start):
        # 방문한 노드를 저장할 셋
        visited = set()

        # 탐색시 맨 처음 방문할 노드 푸시하고 방문 처리
        queue = deque([start])
        visited.add(start)
        result.append(start)
        # 큐가 비어 있지 않은 동안 반복
        while queue:
            # 큐에 있는 원소 중 가장 먼저 푸시된 원소 pop
            node = queue.popleft()
            # 인접한 이웃 노드들에 대해서
            for neighbor in adj_list.get(node, []):
                # 방문되지 않은 인접한 노드인 경우
                if neighbor not in visited:
                    # 인접한 노드를 방문 처리
                    queue.append(neighbor)
                    visited.add(neighbor)
                    result.append(neighbor)

    result = []
    # 시작 노드부터 BFS 탐색 수행
    bfs(start)
    return result
