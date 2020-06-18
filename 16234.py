# 삼성 A형 기출 문제 16234번 인구 이동
def solve(x, y):
    for p in range(4):
        next_x = x + dx[p]
        next_y = y + dy[p]
        if 0 <= next_x < N and 0 <= next_y < N:
            if L <= abs(country_map[next_x][next_y] - country_map[x][y]) <= R:
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = 1
                    stack.append([next_x, next_y])
                    solve(next_x, next_y)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, L, R = map(int, input().split())
country_map = [list(map(int, input().split())) for _ in range(N)]
stack = []
result = 0
while True:
    visited = [[0]*N for _ in range(N)]
    temp = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                stack = [[i, j]]
                solve(i, j)
            if len(stack) > 1:
                temp = 1
                temp_sum = 0
                for q in range(len(stack)):
                    temp_sum += country_map[stack[q][0]][stack[q][1]]
                for a in range(len(stack)):
                    country_map[stack[a][0]][stack[a][1]] = temp_sum // len(stack)
    if temp == 0:
        break
    else:
        result += 1

print(result)