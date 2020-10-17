# 마법사 상어와 파이어볼

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
magic_map = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    magic_map[r-1][c-1].append([m, s, d])

while K > 0:
    fireball_list = []
    for i in range(N):  # 모든 파이어볼이 자신의 방향으로 자신의 속력만큼 이동한다.
        for j in range(N):
            while magic_map[i][j]:
                fireball = magic_map[i][j].pop()
                fireball.append(i)
                fireball.append(j)
                fireball_list.append(fireball)

    while fireball_list:
        fireball = fireball_list.pop()
        next_x = (fireball[3]+dx[fireball[2]]*fireball[1]) % N
        next_y = (fireball[4]+dy[fireball[2]]*fireball[1]) % N
        if next_x < 0:
            next_x = N + next_x
        if next_y < 0:
            next_y = N + next_y
        magic_map[next_x][next_y].append(fireball[:3])

    for i in range(N):
        for j in range(N):
            if len(magic_map[i][j]) > 1:  # 2개 이상의 파이어볼이 있는 곳
                cnt = len(magic_map[i][j])
                m_sum, s_sum = 0, 0
                if magic_map[i][j][0][2] % 2 == 0:
                    flag = 1  # 짝수
                else:
                    flag = 0  # 홀수
                while magic_map[i][j]:
                    fireball = magic_map[i][j].pop()
                    m_sum += fireball[0]
                    s_sum += fireball[1]
                    if flag == 1:  # 짝수인 경우
                        if fireball[2] % 2 != 0:
                            flag = 3
                    elif flag == 0:  # 홀수인 경우
                        if fireball[2] %2 == 0:
                            flag = 3
                if m_sum // 5 != 0:  # 질량이 0이 아니고
                    if flag != 3:  # 합쳐지는 파이어볼의 방향이 짝수이거나 홀수인경우
                        for l in [0, 2, 4, 6]:
                            magic_map[i][j].append([m_sum//5, s_sum//cnt, l])
                    else:
                        for l in [1, 3, 5 ,7]:
                            magic_map[i][j].append([m_sum//5, s_sum//cnt, l])
    K -= 1

result = 0
for i in range(N):
    for j in range(N):
        for fireball in magic_map[i][j]:
            result += fireball[0]

print(result)