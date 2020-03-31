# gaaaaaaaaaaarden
from itertools import combinations


N, M, G, R = map(int, input().split())
map = [list(input().split()) for _ in range(N)]
green_visited = [[0]*M for _ in range(N)]
red_visited = [[0]*M for _ in range(N)]
start, stack = [], []
for i in range(N):
    for j in range(M):
        if map[i][j] == '2':
            start.append([i, j])
for num in combinations(start, G):
    stack.append(list(num))
print(start)
print(stack)