# 삼성 A형 코딩테스트 기출 2048(EASY)
import copy


def is_wall(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def board_sum(x, y, di, board_list):    # 인접한 숫자 합치기
    next_x = x - dx[di]
    next_y = y - dy[di]
    if is_wall(next_x, next_y):
        if board_list[next_x][next_y] != 0:
            if board_list[next_x][next_y] == board_list[x][y]:
                board_list[x][y] *= 2
                board_list[next_x][next_y] = 0
        else:
            while board_list[next_x][next_y] == 0:
                next_x -= dx[di]
                next_y -= dy[di]
                if not is_wall(next_x, next_y):
                    break
                else:
                    if board_list[next_x][next_y] == board_list[x][y]:
                        board_list[x][y] *= 2
                        board_list[next_x][next_y] = 0


def blank(x, y, di, board_list):
    next_x = x + dx[di]
    next_y = y + dy[di]
    temp = board_list[x][y]
    if is_wall(next_x, next_y):
        while board_list[next_x][next_y] == 0:
            board_list[next_x][next_y] = temp
            board_list[next_x - dx[di]][next_y - dy[di]] = 0
            next_x += dx[di]
            next_y += dy[di]
            if not is_wall(next_x, next_y):
                break


def push(bm, depth, direction):
    board_list = copy.deepcopy(bm)
    if direction == 0: # 위로 보내기
        for i in range(N-1):  # 먼저 위 아래로 인접한 같은 숫자를 합치고
            for j in range(N):
                if board_list[i][j] != 0:
                    board_sum(i, j, 0, board_list)

        for i in range(1, N): # 빈 공간을 밀어주기
            for j in range(N):
                if board_list[i][j] != 0:
                    blank(i, j, 0, board_list)

    if direction == 1:  # 아래로 보내기
        for i in range(N-1, 0, -1):  # 먼저 위 아래로 인접한 같은 숫자를 합치고
            for j in range(N):
                if board_list[i][j] != 0:
                    board_sum(i, j, 1, board_list)
        for i in range(N-2, -1, -1):
            for j in range(N):
                if board_list[i][j] != 0:
                    blank(i, j, 1, board_list)

    if direction == 2: # 왼쪽으로 보내기
        for i in range(N):   # 좌우로 인접한 같은 숫자를 합치고
            for j in range(N-1):
                if board_list[i][j] != 0:
                    board_sum(i, j, 2, board_list)
        for i in range(N):
            for j in range(1, N):
                if board_list[i][j] != 0:
                    blank(i, j, 2, board_list)

    if direction == 3:
        for i in range(N):
            for j in range(N-1, 0, -1):
                if board_list[i][j] != 0:
                    board_sum(i, j, 3, board_list)
        for i in range(N):
            for j in range(N-2, -1, -1):
                if board_list[i][j] != 0:
                    blank(i, j, 3, board_list)
    solve(board_list, depth+1)


def solve(m, d):
    global max_value
    board_map = copy.deepcopy(m)
    if d == 5:
        for i in range(N):
            temp = max(board_map[i])
            if temp > max_value:
                max_value = temp
        return
    push(board_map, d, 0)
    push(board_map, d, 1)
    push(board_map, d, 2)
    push(board_map, d, 3)


dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_value = 0
solve(board, 0)
print(max_value)