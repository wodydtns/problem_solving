from collections import deque

def solution(info, edges):
    # 트리 구축 함수
    def build_tree(info, edges):
        tree = [[] for _ in range(len(info)) ]
        for edge in edges:
            tree[edge[0]].append(edge[1])
        return tree
    
    # 트리 생성
    tree = build_tree(info, edges)
    max_sheep = 0 # 최대 양의 수를 저장할 변수 초기화

    # BFS를 위한 큐 생성 및 초기 상태 설정
    q = deque([(0,1,0,set())])

    # BFS 시작
    while q:
        # 큐에서 상태 가져오기
        current, sheep_count, wolf_count, visited = q.popleft()
        # 최대 양의 수 업데이트
        max_sheep = max(max_sheep, sheep_count)

        # 방문한 노드 집합에 현재 노드의 이웃 노드 추가
        visited.update(tree[current])

        # 인접한 노드들에 대해 탐색
        for next_node in visited:
            # 늑대일 경우
            if info[next_node]:
                if sheep_count != wolf_count + 1:
                    q.append(
                        (next_node, sheep_count, wolf_count+1, visited - {next_node})
                    )
                else:
                    q.append(
                        (next_node, sheep_count, wolf_count, visited - {next_node})
                    )
        return max_sheep