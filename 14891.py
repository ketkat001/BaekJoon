# 삼성 A형 코딩 테스트 기출 : 톱니바퀴
def solve(idx, di):
    if idx < 0 or idx > 3 or visited[idx]:  # 종료조건
        return
    visited[idx] = 1
    left = idx - 1
    right = idx + 1
    if di == 1:  # 시계 방향으로 돌 때
        gear[idx] = gear[idx][7:8] + gear[idx][0:7]
        if right < 4:
            if gear[idx][3] != gear[idx+1][6]:  # 오른쪽 톱니바퀴와 다른 극일 경우
                solve(idx+1, -1)
        if left > -1:
            if gear[idx][7] != gear[idx-1][2]:  # 왼쪽 톱니바퀴와 다른 극일 경우
                solve(idx-1, -1)
    else:
        gear[idx] = gear[idx][1:8] + gear[idx][0:1]
        if right < 4:
            if gear[idx][1] != gear[idx+1][6]:  # 오른쪽 톱니바퀴와 다른 극일 경우
                solve(idx+1, 1)
        if left > -1:
            if gear[idx][5] != gear[idx-1][2]:  # 왼쪽 톱니바퀴와 다른 극일 경우
                solve(idx-1, 1)


gear = [list(input()) for _ in range(4)]
for i in range(int(input())):
    index, direction = map(int, input().split())
    visited = [0, 0, 0, 0]
    solve(index-1, direction)
result = 0
for j in range(4):
    if gear[j][0] == '1':
        result += pow(2, j)
print(result)