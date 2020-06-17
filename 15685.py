# 삼성 A형 코딩테스트 기출  드래곤 커브

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(input())
square = [[0]*101 for _ in range(101)]
for _ in range(N):
    y, x, d, g = map(int, input().split())
    direction = [d]
    while g != 0:
        p = len(direction)
        for i in range(p-1, -1, -1):
            direction.append((direction[i]+1) % 4)
        g -= 1
    square[y][x] = 1
    while direction:
        a = direction.pop(0)
        x = x + dx[a]
        y = y + dy[a]
        square[y][x] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if square[i][j] == 1:
            if square[i][j] + square[i+1][j] + square[i+1][j+1] + square[i][j+1] == 4:
                cnt += 1
print(cnt)


