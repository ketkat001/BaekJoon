# 삼성 A형 기출 문제 17144번 미세먼지 안녕!

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
air_clean = []
for i in range(R):
    if room[i][0] == -1:
        air_clean.append(i)
while T != 0:
    temp_room = [[0]*C for _ in range(R)]
    for clean in air_clean:
        temp_room[clean][0] = -1
    # 미세먼지 확산
    for p in range(R):
        for q in range(C):
            if room[p][q] != 0 and room[p][q] != -1:
                cnt = 0
                for di in range(4):
                    n_x, n_y = p + dx[di], q + dy[di]
                    if 0 <= n_x < R and 0 <= n_y < C:
                        if room[n_x][n_y] != -1:
                            temp_room[n_x][n_y] += room[p][q] // 5
                            cnt += 1
                temp_room[p][q] += room[p][q] - ((room[p][q] // 5) * cnt)

    # 공기 청정기 바람(위)
    x_idx = air_clean[0]
    temp_room2 = [[0]*C for _ in range(R)]
    temp_room2[x_idx][0] = -1
    for w in range(2, C):  # 오른쪽 진행
        temp_room2[x_idx][w] = temp_room[x_idx][w-1]
    for e in range(x_idx-1, -1, -1):  # 위쪽 진행
        temp_room2[e][C-1] = temp_room[e+1][C-1]
    for u in range(C-2, -1, -1):  # 왼쪽 진행
        temp_room2[0][u] = temp_room[0][u+1]
    for f in range(1, x_idx):  # 아래쪽 진행
        temp_room2[f][0] = temp_room[f-1][0]

    # 공기 청정기 바람(아래)
    x_idx = air_clean[1]
    temp_room2[x_idx][0] = -1
    for w in range(2, C):  # 오른쪽 진행
        temp_room2[x_idx][w] = temp_room[x_idx][w-1]
    for e in range(x_idx+1, R):  # 아래쪽 진행
        temp_room2[e][C-1] = temp_room[e-1][C-1]
    for u in range(C-2, -1, -1):  # 왼쪽 진행
        temp_room2[R-1][u] = temp_room[R-1][u+1]
    for f in range(R-2, x_idx, -1):  # 위쪽 진행
        temp_room2[f][0] = temp_room[f+1][0]

    # 순환이 되지 않은 미세먼지 입력
    for b in range(1, air_clean[0]):
        temp_room2[b][1:C-1] = temp_room[b][1:C-1]
    for c in range(air_clean[1]+1, R-1):
        temp_room2[c][1:C-1] = temp_room[c][1:C-1]
    room = temp_room2
    T -= 1


result = 0
for m in range(R):
    for n in range(C):
        if room[m][n] != -1:
            result += room[m][n]
print(result)

