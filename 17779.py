# 삼성 A형 코딩테스트 : 게리맨더링2
def solve(x, y, d1, d2):
    global result
    city_zone = [[0] * N for _ in range(N)]
    for p in range(d1+1):
        city_zone[x+p][y-p] = 5
        city_zone[x+d2+p][y+d2-p] = 5
    for q in range(d2+1):
        city_zone[x+q][y+q] = 5
        city_zone[x+d1+q][y-d1+q] = 5
    for i in range(N):
        for j in range(N):
            if city_zone[i][j] == 5:
                next_j = j + 1
                while True:
                    if sum(city_zone[i]) == 5:
                        break
                    if 0 <= next_j < N:
                        if city_zone[i][next_j] != 5:
                            city_zone[i][next_j] = 5
                            next_j += 1
                        else:
                            break
                break
    city_one = 0
    for i in range(x+d1):
        for j in range(y+1):
            if city_zone[i][j] != 5:
                city_one += city[i][j]

    city_two = 0
    for i in range(x+d2+1):
        for j in range(y+1, N):
            if city_zone[i][j] != 5:
                city_two += city[i][j]

    city_three = 0
    for i in range(x+d1, N):
        for j in range(y-d1+d2):
            if city_zone[i][j] != 5:
                city_three += city[i][j]

    city_four = 0
    for i in range(x+d2+1, N):
        for j in range(y-d1+d2, N):
            if city_zone[i][j] != 5:
                city_four += city[i][j]

    city_five = 0
    for i in range(N):
        for j in range(N):
            if city_zone[i][j] == 5:
                city_five += city[i][j]

    cha = max(city_one, city_two, city_three, city_four, city_five) - min(city_one, city_two, city_three, city_four, city_five)
    if result > cha:
        result = cha


N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')
for a in range(N-1):  # x
    for b in range(1, N-1):  # y
        c = 1  # d1
        while True:
            d = 1  # d2
            if c <= N-a-d and c <= b:
                while True:
                    if d < N-a-c and d < N-b:
                        solve(a, b, c, d)
                        d += 1
                    else:
                        break
                c += 1
            else:
                break
print(result)