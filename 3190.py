# 삼성 A형 코딩 테스트 기출 : 뱀
import sys
sys.setrecursionlimit(10000)


def is_wall(x, y):
    if 0 <= x < N and 0 <= y < N:
        if board[x][y] != 1:
            return True
        return False
    return False


def solve(t, x1, y1, d):           # t는 시간, x1,y1은 머리의 좌표 d는 방향
    global result
    if t in time_list:    # time_list 안에 있는 시간에 도달하면
        h = dir_list.pop(0)   # 방향 리스트에서 명령어를 꺼내옴
        if h == 'D':
            if d == 3:
                d = 1
            elif d == 2:
                d = 0
            elif d == 1:
                d = 2
            else:
                d = 3
        else:
            if d == 3:
                d = 0
            elif d == 2:
                d = 1
            elif d == 1:
                d = 3
            else:
                d = 2
    next_x, next_y = x1 + dx[d], y1 + dy[d]
    if is_wall(next_x, next_y):
        if board[next_x][next_y] == 2:
            board[next_x][next_y] = 1
            idx_list.append([next_x, next_y])
        else:
            board[next_x][next_y] = 1
            idx_list.append([next_x, next_y])
            x2, y2 = idx_list.pop(0)
            board[x2][y2] = 0
        solve(t+1, next_x, next_y, d)
    else:
        result = t + 1
    return


dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2
L = int(input())
time_list = []
dir_list = []
for _ in range(L):
    X, C = input().split()
    time_list.append(int(X))
    dir_list.append(C)

s_x, s_y = 0, 0     # 뱀의 머리 위치 인덱스
direction = 3       # 방향 시작 : 오른쪽
idx_list = [[s_x, s_y]]     # 뱀이 지나간 인덱스 저장 * 꼬리 위치를 변경해주기 위해 사용
board[s_x][s_y] = 1
result = 0
solve(0, s_x, s_y, direction)
print(result)

