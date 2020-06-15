# 삼성 A형 코딩테스트 : 로봇 청소기
import sys
sys.setrecursionlimit(100000)


def is_wall(x, y):
    if 0 <= x < N and 0 <= y < M:
        if room[x][y] == 0 and not visited[x][y]:
            return True
    return False


def solve(x, y, direction):
    global cnt
    a = 0
    while a != 4:
        direction = (direction + 3) % 4
        next_x = x + dx[direction]
        next_y = y + dy[direction]
        if is_wall(next_x, next_y):
            visited[next_x][next_y] = 1
            cnt += 1
            solve(next_x, next_y, direction)
            break
        else:
            a += 1

    if a == 4:
        direction = direction - 2
        next_x = x + dx[direction]
        next_y = y + dy[direction]
        if 0 <= next_x < N and 0 <= next_y < M:
            if room[next_x][next_y] == 1:
                return
            else:
                solve(next_x, next_y, direction+2)
    return


dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]  # 0 1 2 3 (index)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[r][c] = 1
cnt = 1
solve(r, c, d)
print(cnt)