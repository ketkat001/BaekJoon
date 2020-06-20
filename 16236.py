# 삼성 A형 기출 문제 16236번 아기상어
from collections import deque


def move(x, y, size, t, eat):
    global result
    queue = deque()
    queue.append([x, y, t])
    ocean[x][y] = 0
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    temp = 0
    eating_list = []
    while queue:
        p, q, time = queue.popleft()
        if temp != 0 and temp != time + 1:
            break
        for di in range(4):
            n_x, n_y = p + dx[di], q + dy[di]
            if (0 <= n_x < N and 0 <= n_y < N) and visited[n_x][n_y] == 0:
                if 0 < ocean[n_x][n_y] < size:
                    eating_list.append([n_x, n_y])
                    temp = time + 1
                    visited[n_x][n_y] = time + 1
                elif ocean[n_x][n_y] == size:
                    visited[n_x][n_y] = time + 1
                    queue.append([n_x, n_y, time + 1])
                elif ocean[n_x][n_y] == 0:
                    queue.append([n_x, n_y, time + 1])
                    visited[n_x][n_y] = time + 1
    if not eating_list:
        result = t
        return
    eating_list = sorted(eating_list, key=lambda x: (x[0], x[1]))
    eat += 1
    ocean[eating_list[0][0]][eating_list[0][1]] = 9
    if eat == size:
        size += 1
        eat = 0
    move(eating_list[0][0], eating_list[0][1], size, temp, eat)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
ocean = [list(map(int, input().split())) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        if ocean[i][j] == 9:
            move(i, j, 2, 0, 0)
print(result)