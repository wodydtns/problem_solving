from collections import defaultdict


def solution(graph, start):
    # 그래프를 인접 리스트로 변환
    adj_list = defaultdict(list)

    for u, v in graph:
        adj_list[u].append(v)

    # DFS 탐색 함수
    def dfs(node, visited, result):
        # 현재 노드를 방문한 노드들의 집합에 추가
        visited.add(node)

        # 현재 노드를 결과 리스트에 추가
        result.append(node)

        # 현재 노드와 인접합 노드 순회
        for neighbor in adj_list.get(node, []):
            # 아직 방문하지 않은 노드라면
            if neighbor not in visited:
                dfs(neighbor, visited, result)

    # DFS를 순회한 결과를 반환
    visited = set()
    result = []
    # 시작 노드에서 깊이 우선 탐색 시작
    dfs(start, visited, result)
    return result
