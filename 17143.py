# 삼성 A형 코딩테스트 : 낚시왕
def solve(w, ss, shark_map):
    global result
    if w == C:
        result = ss
        return
    else:
        w += 1
        temp = 0
        for p in range(R+1):
            if shark_map[p][w] != 0:
                temp = shark_map[p][w][2]
                shark_map[p][w] = 0
                break
        temp_list = [[0]*(C+1) for _ in range(R+1)]
        for i in range(R+1):
            for j in range(C+1):
                if shark_map[i][j] != 0:
                    direction = shark_map[i][j][1]
                    if direction == 1 or direction == 2:
                        cnt = shark_map[i][j][0] % (2*(R-1))
                    else:
                        cnt = shark_map[i][j][0] % (2*(C-1))
                    next_x, next_y = i, j
                    while cnt > 0:
                        if direction == 1:
                            if next_x == 1:
                                direction = 2
                            next_x += dx[direction]
                            next_y += dy[direction]
                            if next_x == 1:
                                direction = 2
                        elif direction == 2:
                            if next_x == R:
                                direction = 1
                            next_x += dx[direction]
                            next_y += dy[direction]
                            if next_x == R:
                                direction = 1
                        elif direction == 3:
                            if next_y == C:
                                direction = 4
                            next_x += dx[direction]
                            next_y += dy[direction]
                            if next_y == C:
                                direction = 4
                        elif direction == 4:
                            if next_y == 1:
                                direction = 3
                            next_x += dx[direction]
                            next_y += dy[direction]
                            if next_y == 1:
                                direction = 3
                        cnt -= 1
                    if temp_list[next_x][next_y] == 0:
                        temp_list[next_x][next_y] = [shark_map[i][j][0], direction, shark_map[i][j][2]]
                    else:
                        if temp_list[next_x][next_y][2] < shark_map[i][j][2]:
                            temp_list[next_x][next_y] = [shark_map[i][j][0], direction, shark_map[i][j][2]]
        solve(w, ss+temp, temp_list)


dx = [0, -1, 1, 0, 0]  # 가운데 위 아래 오른쪽 왼쪽
dy = [0, 0, 0, 1, -1]

R, C, M = map(int, input().split())
shark = [[0]*(C+1) for _ in range(R+1)]
result = 0
for _ in range(M):
    r, c, s, d, z = map(int, input().split())  # s = 속력, d = 방향, z = 크기
    shark[r][c] = [s, d, z]

solve(0, 0, shark)
print(result)