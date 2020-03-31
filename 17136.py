def is_wall(x, y, p):
    if paper_cut[p] > 0 and x <= 10 and y <= 10:
        return True
    return False


def solve(n, s):
    global min_paper
    if s == 0:
        if min_paper > n:
            min_paper = n
    else:
        for i in range(10):
            for j in range(10):
                if paper[i][j] and not visited[i][j]:
                    for p in range(5, 0, -1):
                        if is_wall(i+p, j+p, p):
                            temp = 0
                            for r in range(i, i+p):
                                for c in range(j, j+p):
                                    if visited[r][c] == 0:
                                        temp += paper[r][c]
                            if temp == p*p:
                                for r in range(i, i+p):
                                    for c in range(j, j+p):
                                        visited[r][c] = 1
                                paper_cut[p] -= 1
                                solve(n+1, s-temp)
                                for r in range(i, i+p):
                                    for c in range(j, j+p):
                                        visited[r][c] = 0
                                paper_cut[p] += 1
                    return


paper_cut = [0, 5, 5, 5, 5, 5]
paper = [list(map(int, input().split())) for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
min_paper = 26
paper_sum = 0
for q in range(10):
    paper_sum += sum(paper[q])
if paper_sum > 3:
    solve(0, paper_sum)
    if min_paper == 26:
        result = -1
    else:
        result = min_paper
else:
    result = paper_sum
print(result)
