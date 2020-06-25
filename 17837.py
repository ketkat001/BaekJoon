# 삼성 A형 코딩테스트 : 새로운 게임2

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chess_location = [[] for _ in range(K+1)]
chess = [[[] for _ in range(N)] for _ in range(N)]
for n in range(1, K+1):
    x, y, d = map(int, input().split())
    chess_location[n] = [x-1, y-1, d]
    chess[x-1][y-1].append(n)

t = 1
flag = 0
result = -1
while t < 1001:

    if flag == 1:
        break
    for num in range(1, K+1):
        x1, y1, di = chess_location[num]
        n_x = x1 + dx[di]
        n_y = y1 + dy[di]
        moving = []
        for a in range(len(chess[x1][y1])):
            if chess[x1][y1][a] == num:
                moving = chess[x1][y1][a:]
                for p in moving:
                    chess[x1][y1].pop()
                break
        if 0 <= n_x < N and 0 <= n_y < N:

            if board[n_x][n_y] == 0:
                chess[n_x][n_y] += moving
                if len(chess[n_x][n_y]) >= 4:
                    flag = 1
                    result = t
                    break
                for m in moving:
                    chess_location[m][0] = n_x
                    chess_location[m][1] = n_y
            elif board[n_x][n_y] == 1:
                moving.reverse()
                chess[n_x][n_y] += moving
                if len(chess[n_x][n_y]) >= 4:
                    flag = 1
                    result = t
                    break
                for m in moving:
                    chess_location[m][0] = n_x
                    chess_location[m][1] = n_y
            else:
                if di == 1 or di == 3:
                    di += 1
                else:
                    di -= 1
                chess_location[num][2] = di
                next_x = x1 + dx[di]
                next_y = y1 + dy[di]
                if 0 <= next_x < N and 0 <= next_y < N:
                    if board[next_x][next_y] == 0:
                        chess[next_x][next_y] += moving
                        if len(chess[next_x][next_y]) >= 4:
                            flag = 1
                            result = t
                            break
                        for m in moving:
                            chess_location[m][0] = next_x
                            chess_location[m][1] = next_y
                    elif board[next_x][next_y] == 1:
                        moving.reverse()
                        chess[next_x][next_y] += moving
                        if len(chess[next_x][next_y]) >= 4:
                            flag = 1
                            result = t
                            break
                        for m in moving:
                            chess_location[m][0] = next_x
                            chess_location[m][1] = next_y
                    else:
                        chess[x1][y1] += moving
                else:
                    chess[x1][y1] += moving
        else:
            if di == 1 or di == 3:
                di += 1
            else:
                di -= 1
            chess_location[num][2] = di
            next_x = x1 + dx[di]
            next_y = y1 + dy[di]
            if 0 <= next_x < N and 0 <= next_y < N:
                if board[next_x][next_y] == 0:
                    chess[next_x][next_y] += moving
                    if len(chess[next_x][next_y]) >= 4:
                        flag = 1
                        result = t
                        break
                    for m in moving:
                        chess_location[m][0] = next_x
                        chess_location[m][1] = next_y
                elif board[next_x][next_y] == 1:
                    moving.reverse()
                    chess[next_x][next_y] += moving
                    if len(chess[next_x][next_y]) >= 4:
                        flag = 1
                        result = t
                        break
                    for m in moving:
                        chess_location[m][0] = next_x
                        chess_location[m][1] = next_y
                else:
                    chess[x1][y1] += moving
    t += 1
print(result)