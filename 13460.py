# 삼성 A형 코딩 테스트 기출 : 구슬 탈출 2
from collections import deque


def push(x, y, di):
    count = 0
    while board[x+dx[di]][y+dy[di]] != '#' and board[x][y] != 'O':
        x = x+dx[di]
        y = y+dy[di]
        count += 1
    return x, y, count


def solve():
    global result
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d >= 10:
            return
        for direction in range(4):
            red_x, red_y, red_move = push(rx, ry, direction)
            blue_x, blue_y, blue_move = push(bx, by, direction)
            if board[blue_x][blue_y] == 'O':
                continue
            if board[red_x][red_y] == 'O':
                result = d + 1
                return
            if red_x == blue_x and red_y == blue_y:       # 두 구슬이 같은 곳에 동시에 존재할때
                if red_move > blue_move:                 # 많이 움직인 구슬을 한칸 뒤로
                    red_x -= dx[direction]
                    red_y -= dy[direction]
                else:
                    blue_x -= dx[direction]
                    blue_y -= dy[direction]
            if [red_x, red_y, blue_x, blue_y] not in visit:
                q.append([red_x, red_y, blue_x, blue_y, d+1])
                visit.append([red_x, red_y, blue_x, blue_y])


dx = [-1, 1, 0, 0]   # 상하좌우
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
q = deque()
visit = []
result = -1
r_x, r_y, b_x, b_y = 0, 0, 0, 0
for i in range(N):       # 파란공과 빨간공의 시작 위치 저장
    for j in range(M):
        if board[i][j] == 'B':
            b_x, b_y = i, j

        if board[i][j] == 'R':
            r_x, r_y = i, j
q.append([r_x, r_y, b_x, b_y, 0])
visit.append([r_x, r_y, b_x, b_y])
solve()

print(result)