# 백준 1926번 그림
import sys
sys.setrecursionlimit(250000)


def solve(x, y):
    global s
    for d in range(4):
        next_x = x + dx[d]
        next_y = y + dy[d]
        if 0 <= next_x < n and 0 <= next_y < m:
            if not visited[next_x][next_y] and art_map[next_x][next_y] == '1':
                visited[next_x][next_y] = 1
                s += 1
                solve(next_x, next_y)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
art_map = [list(input().split()) for _ in range(n)]
art_cnt, max_art = 0, 0
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and art_map[i][j] == '1':
            s = 1
            visited[i][j] = 1
            art_cnt += 1
            solve(i, j)
            if s > max_art:
                max_art = s
print(art_cnt)
print(max_art)

