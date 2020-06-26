# 삼성 A형 코딩테스트 19237번 : 어른 상어

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

N, M, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]  # 맵
shark_direction = [0] + list(map(int, input().split()))  # 상어의 현재 방향
shark_priority = [[[] for _ in range(5)] for _ in range(M+1)]  # 상어 움직임의 우선순위
shark_visited = [[[] for _ in range(N)] for _ in range(N)]  # 상어의 냄새(방문)와 남은 시간
for i in range(1, M+1):
    for j in range(1, 5):
        shark_priority[i][j] = list(map(int, input().split()))

shark_location = [[] for _ in range(M+1)]   # 상어의 위치와 방향을 합침
for n in range(1, M+1):
    for x in range(N):
        for y in range(N):
            if board[x][y] == n:
                shark_location[n] = [x, y, shark_direction[n]]
                shark_visited[x][y] = [n, k]
t = 1
result = -1
while t < 1001:
    temp_list = []
    for num in range(1, M+1):
        if shark_location[num]:
            x1, y1, di = shark_location[num]
            shark_location[num] = []
            flag = 0
            while True:
                if flag == 1:
                    break
                priority = shark_priority[num][di]
                for d in priority:
                    nx = x1 + dx[d]
                    ny = y1 + dy[d]
                    if 0 <= nx < N and 0 <= ny < N and not shark_visited[nx][ny]:
                        if board[nx][ny] != 0:
                            if board[nx][ny] > num:
                                shark_location[num] = [nx, ny, d]
                                board[nx][ny], board[x1][y1] = num, 0
                                temp_list.append([nx, ny, num, k])
                            else:
                                board[x1][y1] = 0
                        else:
                            shark_location[num] = [nx, ny, d]
                            board[nx][ny], board[x1][y1] = num, 0
                            temp_list.append([nx, ny, num, k])
                        flag = 1
                        break
                else:
                    for d in priority:
                        nx = x1 + dx[d]
                        ny = y1 + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            if shark_visited[nx][ny][0] == num:
                                shark_location[num] = [nx, ny, d]
                                board[nx][ny], board[x1][y1] = num, 0
                                temp_list.append([nx, ny, num, k])
                                flag = 1
                                break

    for m in range(N):   # 상어가 k번 이동하면 냄새를 없애줌
        for b in range(N):
            if shark_visited[m][b]:
                shark_visited[m][b][1] -= 1
                if shark_visited[m][b][1] == 0:
                    shark_visited[m][b] = []
    for temp in temp_list:
        shark_visited[temp[0]][temp[1]] = [temp[2], temp[3]]
    shark_sum = 0
    for i in range(N):
        shark_sum += sum(board[i])
    if shark_sum == 1:
        result = t
        break
    t += 1

print(result)