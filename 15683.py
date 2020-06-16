# 삼성 A형 코딩테스트 기출 : 감시
import copy


def cctv_range(x, y, d, office_m):
    while 0 <= x < N and 0 <= y < M:
        if office_m[x][y] == '6':
            return
        if office_m[x][y] == '0':
            office_m[x][y] = '#'
        x += dx[d]
        y += dy[d]


def solve(office_map, state):
    for i in range(N):
        print(office_map[i])
    print()
    global min_value
    if state == len(queue):
        cnt = 0
        for p in range(N):
            for q in range(M):
                if office_map[p][q] == '0':
                    cnt += 1
        if min_value > cnt:
            min_value = cnt
        return
    cctv, cctv_x, cctv_y = queue[state]
    if cctv == '1':
        for di in range(4):
            office_m = copy.deepcopy(office_map)
            next_x = cctv_x + dx[di]
            next_y = cctv_y + dy[di]
            cctv_range(next_x, next_y, di, office_m)
            solve(office_m, state+1)

    elif cctv == '2':
        for di in range(2):
            office_m = copy.deepcopy(office_map)
            next_x = cctv_x + dx[di]
            next_y = cctv_y + dy[di]
            cctv_range(next_x, next_y, di, office_m)
            next_x2 = cctv_x + dx[(di + 2) % 4]
            next_y2 = cctv_y + dy[(di + 2) % 4]
            cctv_range(next_x2, next_y2, (di + 2) % 4, office_m)
            solve(office_m, state+1)

    elif cctv == '3':
        for di in range(4):
            office_m = copy.deepcopy(office_map)
            next_x = cctv_x + dx[di]
            next_y = cctv_y + dy[di]
            cctv_range(next_x, next_y, di, office_m)
            next_x2 = cctv_x + dx[(di + 1) % 4]
            next_y2 = cctv_y + dy[(di + 1) % 4]
            cctv_range(next_x2, next_y2, (di + 1) % 4, office_m)
            solve(office_m, state+1)

    elif cctv == '4':
        for di in range(4):
            office_m = copy.deepcopy(office_map)
            next_x = cctv_x + dx[di]
            next_y = cctv_y + dy[di]
            cctv_range(next_x, next_y, di, office_m)
            next_x2 = cctv_x + dx[(di + 1) % 4]
            next_y2 = cctv_y + dy[(di + 1) % 4]
            cctv_range(next_x2, next_y2, (di + 1) % 4, office_m)
            next_x3 = cctv_x + dx[(di + 2) % 4]
            next_y3 = cctv_y + dy[(di + 2) % 4]
            cctv_range(next_x3, next_y3, (di + 2) % 4, office_m)
            solve(office_m, state+1)
    else:
        office_m = copy.deepcopy(office_map)
        for di in range(4):
            next_x = cctv_x + dx[di]
            next_y = cctv_y + dy[di]
            cctv_range(next_x, next_y, di, office_m)
        solve(office_m, state+1)


dx = [1, 0, -1, 0]  # 상 우 하 좌  시계방향
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
office = [list(input().split()) for _ in range(N)]
queue = []
min_value = N * M
for i in range(N):
    for j in range(M):
        if office[i][j] != '0' and office[i][j] != '6':
            queue.append([office[i][j], i, j])
solve(office, 0)
print(min_value)