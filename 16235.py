# 삼성 A형 기출 문제 16235번 나무 재테크
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
N, M, K = map(int, input().split())
map_list = [[5]*N for _ in range(N)]
food_list = [list(map(int, input().split())) for _ in range(N)]
tree_list = [[[]*N for _ in range(N)] for _ in range(N)]
for m in range(M):
    x, y, z = map(int, input().split())
    tree_list[x-1][y-1].append(z)
while K != 0:
    # 봄
    for i in range(N):
        for j in range(N):
            tree_list[i][j].sort()
            idx = 0
            while True:
                if idx >= len(tree_list[i][j]):
                    break
                if map_list[i][j] >= tree_list[i][j][idx]:
                    map_list[i][j] -= tree_list[i][j][idx]
                    tree_list[i][j][idx] += 1
                    idx += 1
                else:
                    break
            dead_tree = tree_list[i][j][idx:]
            tree_list[i][j] = tree_list[i][j][:idx]
            for d_tree in dead_tree:
                map_list[i][j] += d_tree // 2

    # 가을
    for i in range(N):
        for j in range(N):
            for q in range(len(tree_list[i][j])):
                if tree_list[i][j][q] % 5 == 0:
                    for d in range(8):
                        next_x = i + dx[d]
                        next_y = j + dy[d]
                        if 0 <= next_x < N and 0 <= next_y < N:
                            tree_list[next_x][next_y].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            map_list[i][j] += food_list[i][j]

    K -= 1

result = 0
for i in range(N):
    for j in range(N):
        result += len(tree_list[i][j])

print(result)


