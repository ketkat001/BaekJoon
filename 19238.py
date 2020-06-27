# 삼성 역량 테스트 기출 : 스타트 택시
from collections import deque


def psg(x, y):
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append([x, y])
    temp = 99999
    t_q = []
    while queue:
        tx, ty = queue.popleft()
        if temp < visited[tx][ty]:
            break
        if [tx, ty] in passenger:
            temp = visited[tx][ty]
            t_q.append([tx, ty])
        else:
            for d in range(4):
                n_x, n_y = tx + dx[d], ty + dy[d]
                if 0 <= n_x < N and 0 <= n_y < N and board[n_x][n_y] != 1 and visited[n_x][n_y] == 0:
                    queue.append([n_x, n_y])
                    visited[n_x][n_y] = visited[tx][ty] + 1
    if t_q:
        t_l = sorted(t_q, key=lambda x: (x[0], x[1]))
        return visited[t_l[0][0]][t_l[0][1]], t_l[0][0], t_l[0][1]
    else:
        return -1, -1, -1


def dtn(x, y, index):
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append([x, y])
    while queue:
        tx, ty = queue.popleft()
        if destination[index] == [tx, ty]:
            break
        else:
            for d in range(4):
                n_x, n_y = tx + dx[d], ty + dy[d]
                if 0 <= n_x < N and 0 <= n_y < N and board[n_x][n_y] != 1 and visited[n_x][n_y] == 0:
                    queue.append([n_x, n_y])
                    visited[n_x][n_y] = visited[tx][ty] + 1
    return visited[tx][ty], tx, ty


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M, F = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
t_x, t_y = map(int, input().split())
t_x, t_y = t_x - 1, t_y - 1
passenger = []
destination = []
for _ in range(M):
    p_x, p_y, d_x, d_y = map(int, input().split())
    passenger.append([p_x - 1, p_y - 1])
    destination.append([d_x - 1, d_y - 1])
for _ in range(M):
    fuel, t_x, t_y = psg(t_x, t_y)
    if fuel == -1:
        F = -1
        break
    for i in range(M):
        if passenger[i] == [t_x, t_y]:
            passenger[i] = [-1, -1]
            break
    F -= fuel
    if F < 0:
        F = -1
        break
    fuel, t_x, t_y = dtn(t_x, t_y, i)
    destination[i] = [-1, -1]
    F -= fuel
    if F < 0:
        F = -1
        break
    else:
        F += fuel * 2
print(F)