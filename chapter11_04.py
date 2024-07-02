def solution(graph, source):
    # 그래프의 노드 수
    num_vertices = len(graph)

    # 거리 배열 초기화
    distance = [float("inf")] * num_vertices
    distance[source] = 0

    # 직전 경로 배열 초기화
    predecessor = [None] * num_vertices

    # 간선 수 만큼 반복해 최단 경로 갱신
    for temp in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                # 현재 노드 u를 거쳐서 노드 v로 가는 경로의 거리가 기존에 저장된 노드 v까지의 거리보다 짧은 경우
                if distance[u] + weight < distance[v]:
                    # 최단 거리를 갱신
                    distance[v] = distance[u] + weight
                    # 직전 경로 업데이트
                    predecessor[v] = u

    # 음의 가중치 순회 체크
    for u in range(num_vertices):
        for v, weight in graph[u]:
            # 현재 노드 u를 거쳐서 노드 v로 가는 경로의 거리가 기존에 저장된 노드 v까지의 거리보다 짧은 경우
            if distance[u] + weight < distance[v]:
                # 음의 가중치 순회가 발견되었으므로 [-1] 을 반환
                return [-1]
    return [distance, predecessor]
