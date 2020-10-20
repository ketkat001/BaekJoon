# 컨베이너 벨트 위의 로봇

N, K = map(int, input().split())

conveyor_belt = list(map(int, input().split()))

robots = []
result = 0

while True:
    conveyor_belt = conveyor_belt[2*N-1:] + conveyor_belt[0:2*N-1]  # 벨트가 한칸 회전한다
    for i in range(len(robots)):  # 로봇도 벨트를 따라 한칸 회전한다
        if robots[i] == 2*N-1:
            robots[i] = 0
        else:
            robots[i] += 1
    if N-1 in robots:  # 내려가는 위치에 로봇이 있을 경우 삭제
        robots.remove(N-1)

    for i in range(len(robots)):  # 로봇이 한칸 이동할 수 있다면 이동, 아니라면 가만히 있는다
        if robots[i]+1 == 2*N:
            if 0 not in robots and conveyor_belt[0] > 0:
                conveyor_belt[0] -= 1
                robots[i] = 0
        else:
            if robots[i]+1 not in robots and conveyor_belt[robots[i]+1] > 0:
                conveyor_belt[robots[i]+1] -= 1
                robots[i] += 1

    if N-1 in robots:
        robots.remove(N-1)
    if 0 not in robots and conveyor_belt[0] > 0:  # 올라가는 위치에 로봇이 없다면 로봇 삽입
        robots.append(0)
        conveyor_belt[0] -= 1
    temp = 0
    for i in range(2*N):
        if conveyor_belt[i] == 0:
            temp += 1
    if temp >= K:
        result += 1
        break
    else:
        result += 1

print(result)