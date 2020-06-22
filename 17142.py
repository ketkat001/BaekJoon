# 삼성 A형 코딩테스트 : 연구소 3
from itertools import combinations


def is_wall(x, y, visited):
    if 0 <= x < N and 0 <= y < N:
        if (lab_map[x][y] == 0 or lab_map[x][y] == 2) and visited[x][y] == 0:
            return True
        return False
    return False


def solve(virus_list):
    global result
    visited = [[0] * N for _ in range(N)]
    max_value = 0
    for vir in virus_list:
        visited[vir[0]][vir[1]] = 1
    while virus_list:
        v_x, v_y = virus_list.pop(0)
        for di in range(4):
            next_x = v_x + dx[di]
            next_y = v_y + dy[di]
            if is_wall(next_x, next_y, visited):
                if lab_map[next_x][next_y] == 2:
                    for d in range(4):
                        n_x = next_x + dx[d]
                        n_y = next_y + dy[d]
                        if is_wall(n_x, n_y, visited):
                            visited[next_x][next_y] = visited[v_x][v_y] + 1
                            virus_list.append([next_x, next_y])
                else:
                    visited[next_x][next_y] = visited[v_x][v_y] + 1
                    virus_list.append([next_x, next_y])

    temp = 0
    for p in range(N):
        if temp == 1:
            max_value = -1
            break
        for q in range(N):
            if not visited[p][q] and not lab_map[p][q]:
                temp = 1
                break
            else:
                if lab_map[p][q] != 2:
                    if max_value < visited[p][q]:
                        max_value = visited[p][q]
    if max_value != -1:
        if result == -1:
            result = max_value
        else:
            if result > max_value:
                result = max_value


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N, M = map(int, input().split())
lab_map = [list(map(int , input().split())) for _ in range(N)]

virus = []
result = -1
a = 0
for i in range(N):
    for j in range(N):
        if lab_map[i][j] == 2:
            virus.append([i, j])
        if lab_map[i][j] == 0:
            a = 1

virus_start = list(combinations(virus, M))
for vi in virus_start:
    solve(list(vi))
if result == -1:
    print(result)
elif a == 0:
    print(0)
else:
    print(result-1)