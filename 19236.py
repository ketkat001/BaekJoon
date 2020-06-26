# 삼성 A형 코딩테스트 19236번 : 청소년 상어
import copy


def solve(s_x, s_y, di, s, s_map):
    global result
    move(s_x, s_y, s_map)
    next_eat = []
    next_x, next_y = s_x + dx[di], s_y + dy[di]
    while 0 <= next_x < 4 and 0 <= next_y < 4:
        if s_map[next_x][next_y] != 0:
            next_eat.append([next_x, next_y, s_map[next_x][next_y][1], s_map[next_x][next_y][0]])
        next_x += dx[di]
        next_y += dy[di]
    if not next_eat:
        if s > result:
            result = s
            return
    else:
        for fish in next_eat:
            fish_map = copy.deepcopy(s_map)
            fish_map[fish[0]][fish[1]] = 0
            solve(fish[0], fish[1], fish[2], s+fish[3], fish_map)


def move(sx, sy, s_map):
    for num in range(1, 17):
        x, y, d = -1, -1, -1
        for p in range(4):
            for q in range(4):
                if s_map[p][q] != 0 and s_map[p][q][0] == num:
                    x, y, d = p, q, s_map[p][q][1]
        if x == -1:
            continue
        for _ in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == sx and ny == sy):
                d = (d + 1) % 9
                if d == 0:
                    d = 1
            else:
                s_map[x][y][1] = d
                s_map[x][y], s_map[nx][ny] = s_map[nx][ny], s_map[x][y]
                break


dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
shark_map = []
for i in range(4):
    temp = list(map(int, input().split()))
    tmp = []
    for j in range(4):
        tmp.append([temp[2*j], temp[2*j+1]])
    shark_map.append(tmp)
result = 0
direction, cnt = shark_map[0][0][1], shark_map[0][0][0]
shark_map[0][0] = 0
solve(0, 0, direction, cnt, shark_map)
print(result)