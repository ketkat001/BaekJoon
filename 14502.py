# 삼성 A형 기출문제 / 연구소
from itertools import combinations
import copy


def is_wall(x, y, l):
    if 0 <= x < N and 0 <= y < M and l[x][y] == 0:
        return True
    return False


def solve(a):
    lab = copy.deepcopy(lab_map)
    for p in range(3):   # 벽 세우기
        lab[a[p][0]][a[p][1]] = 1
    virus(lab)


def virus(l):
    global max_value
    cnt = 0
    start = []
    for x in range(N):
        for y in range(M):
            if l[x][y] == 2:
                start.append([x, y])
    while start:
        n, m = start.pop(0)
        for q in range(4):
            next_x = n + dx[q]
            next_y = m + dy[q]
            if is_wall(next_x, next_y, l):
                l[next_x][next_y] = 2
                start.append([next_x, next_y])
    for b in range(N):
        for c in range(M):
            if l[b][c] == 0:
                cnt += 1

    if max_value < cnt:
        max_value = cnt


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(N)]
temp_list = []
max_value = 0

for i in range(N):    # 빈칸인 곳 temp_list에 저장
    for j in range(M):
        if lab_map[i][j] == 0:
            temp_list.append([i, j])

wall_list = list(combinations(temp_list, 3))
for i in range(len(wall_list)):
    solve(wall_list[i])

print(max_value)
