def find(parents, x):
    # 루트 노드 찾는 함수
    # 만약 x의 부모가 자기 자신이면
    if parents[x] == x:
        return x
    # 그렇지 않다면 x의 부모를 찾아서 parents[x]에 저장
    # 그 부모 노드의 루트 노드를 찾아서 parents[x]에 저장
    parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, x, y):
    # 두 개의 집합을 합치는 함수
    # x가 속한 집합의 루트 노드 찾기
    root1 = find(parents, x)
    # y가 속한 집합의 루트 노드 찾기
    root2 = find(parents, y)

    # y가 속한 집합을 x가 속한 집합에 합침
    parents[root2] = root1


def solution(k, operations):
    # 처음에는 각 노드가 자기 자신을 부모로 가지도록 초기화
    parents = list(range(k))

    # 집합의 개수를 저장할 변수, 처음에는 모든 노드가 서로 다른 집합에 있으므로 k
    n = k

    # opertaions 리스트에 있는 연산들을 하나씩 처리
    for op in operations:
        if op[0] == "u":
            # op[1], op[2] 가 속한 집합을 합침
            union(parents, op[1], op[2])
        elif op[0] == "f":
            find(parents, op[1])

    # 모든 노드의 루트 노드를 찾아서 집합의 개수를 계산
    n = len(set(find(parents, i) for i in range(k)))

    return n
