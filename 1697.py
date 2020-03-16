def bfs():
    while queue:
        x = queue.pop(0)
        if x == K:
            break
        next_x1 = x + 1
        next_x2 = x - 1
        next_x3 = x * 2
        if next_x1 < 100001:
            if visited[next_x1] == 0:
                queue.append(next_x1)
                visited[next_x1] = visited[x] + 1
        if 0 <= next_x2 < 100001:
            if visited[next_x2] == 0:
                queue.append(next_x2)
                visited[next_x2] = visited[x] + 1
        if next_x3 < 100001:
            if visited[next_x3] == 0:
                queue.append(next_x3)
                visited[next_x3] = visited[x] + 1
    return visited[K]


N, K = map(int, input().split())
visited = [0] * 100002
queue = [N]
result = bfs()
print(result)
