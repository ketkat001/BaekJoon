# 삼성 A형 코딩 테스트 기출 : 경사로
import sys
sys.setrecursionlimit(100000)


def solve_x(x, y, start, check):
    global result
    if y > N-1:
        if check >= 0:
            result += 1
    else:
        if start < runway[x][y]:  # 첫 높이보다 다음 값이 높다면
            if runway[x][y] - start == 1:
                if check >= L:  # 경사로의 길이보다 check가 길거나 같다면
                    solve_x(x, y+1, runway[x][y], 1)
        elif start == runway[x][y]:  # 다음 값과 높이가 같다면
            solve_x(x, y+1, start, check + 1)
        else:  # 다음 값의 높이가 더 낮다면
            if start - runway[x][y] == 1:
                if check >= 0:
                    solve_x(x, y+1, runway[x][y], -L + 1)


def solve_y(x, y, start, check):
    global result
    if x > N - 1:
        if check >= 0:
            result += 1
    else:
        if start < runway[x][y]:  # 첫 높이보다 다음 값이 높다면
            if runway[x][y] - start == 1:
                if check >= L:  # 경사로의 길이보다 check가 길거나 같다면
                    solve_y(x+1, y, runway[x][y], 1)
        elif start == runway[x][y]:  # 다음 값과 높이가 같다면
            solve_y(x+1, y, start, check + 1)
        else:  # 다음 값의 높이가 더 낮다면
            if start - runway[x][y] == 1:
                if check >= 0:
                    solve_y(x+1, y, runway[x][y], -L + 1)


N, L = map(int, input().split())
runway = [list(map(int, input().split())) for _ in range(N)]
result = 0
for i in range(N):
    solve_x(i, 1, runway[i][0], 1)
    solve_y(1, i, runway[0][i], 1)
print(result)



