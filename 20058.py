# 마법사 상어와 파이어스톰
from collections import deque


def spin_right(l):
    M = len(l)
    res = [[0]*M for _ in range(M)]
    for p in range(M):
        for q in range(M):
            res[p][M-q-1] = l[q][p]
    return res


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, Q = map(int, input().split())
ice_map = [list(map(int, input().split())) for _ in range(2**N)]
Q_list = list(map(int, input().split()))
for L in Q_list:
    size = 2**L
    size_cnt = ((2**N) // size)
    for m in range(size_cnt):  # 회전
        for n in range(size_cnt):
            temp_list = [row[m*size:(m+1)*size] for row in ice_map[n*size:(n+1)*size]]
            temp_list = spin_right(temp_list)
            cnt = 0
            for row in ice_map[n*size:(n+1)*size]:
                row[m*size:(m+1)*size] = temp_list[cnt]
                cnt += 1
    melt = []
    for x in range(2**N):
        for y in range(2**N):
            if ice_map[x][y] == 0:
                continue
            ice_cnt = 0
            for d in range(4):
                next_x, next_y = x + dx[d], y+dy[d]
                if 0 <= next_x < 2**N and 0 <= next_y < 2**N:
                    if ice_map[next_x][next_y] >= 1:
                        ice_cnt += 1
            if ice_cnt < 3:
                melt.append([x, y])
    for me in melt:
        ice_map[me[0]][me[1]] -= 1

sum_result = 0
max_ice = 0
for i in range(2**N):
    sum_result += sum(ice_map[i])

visited = [[0]*(2**N) for _ in range(2**N)]
queue = deque()

for i in range(2**N):
    for j in range(2**N):
        temp_sum = 0
        if ice_map[i][j] != 0 and visited[i][j] == 0:
            queue.append([i, j])
        while queue:
            x, y = queue.popleft()
            visited[x][y] = 1
            temp_sum += 1
            for d in range(4):
                next_x, next_y = x + dx[d], y + dy[d]
                if 0 <= next_x < 2**N and 0 <= next_y < 2**N:
                    if visited[next_x][next_y] == 0 and ice_map[next_x][next_y] != 0:
                        if [next_x, next_y] not in queue:
                            queue.append([next_x, next_y])

        if temp_sum > max_ice:
            max_ice = temp_sum
print(sum_result)
print(max_ice)
