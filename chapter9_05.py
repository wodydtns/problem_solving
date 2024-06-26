from collections import deque

# 이동 가능한 좌표인지 판단하는 함수
def is_valid_move(ny, nx, n,m, maps):
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X"

# 방문한 적이 없으면 큐에 넣고 방문 여부 표시
def append_to_queue(ny,nx,k,time,visited,q):
    if not visited[ny][nx][k]:
        visited[ny][nx][k] = True
        q.append((ny,nx,k,time+1))

def solution(maps):
    n,m = len(maps), len(maps[0])
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    dy = [-1, 1, 0, 0]
    dx = [0,0,-1,1]
    q = deque()
    end_y, end_x = -1, -1

    #시작점과 도착점을 찾아 큐에 넣고 방문 여부 표시
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                #시작점
                q.append((i,j,0,0))
                visited[i][j][0] = True
            if maps[i][j] == "E":
                # 도착점
                end_y, end_x = i, j
    while q:
        # 큐에서 좌표와 이동 횟수를 꺼냄
        y,x,k,time = q.popleft()

        #도착점에 도달하면 결과 반환
        if y == end_y and x == end_x and k == 1:
            return time 

        # 네 방향으로 이동
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 이동 가능한 좌표인 때에만 큐에 넣음
            if not is_valid_move(ny,nx,n,m,maps):
                continue

            # 다음 이동 지점이 벽인 경우
            if maps[ny][nx] == "L":
                append_to_queue(ny, nx, 1, time, visited, q)
            # 다음 이동 지점이 벽이 아닌 경우
            else:
                append_to_queue(ny, nx, k, time, visited, q)
    return -1