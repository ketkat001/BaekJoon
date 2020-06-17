# 삼성 A형 코딩테스트 15686번 치킨 배달

from itertools import combinations
import copy


N, M = map(int, input().split())
chicken = [list(input().split()) for _ in range(N)]
start_list = []
house_list = []
chicken_min = []
for i in range(N):            # 치킨집 리스트에 넣기
    for j in range(N):
        if chicken[i][j] == '2':
            start_list.append([i, j])
        if chicken[i][j] == '1':
            house_list.append([i, j])
for chic in combinations(start_list, M):
    house = copy.deepcopy(house_list)
    chic_sum = 0
    while house:
        house_x, house_y = house.pop()
        temp, chic_distance = 100000, 0
        for p in range(len(chic)):
            chic_distance = abs(house_x - chic[p][0]) + abs(house_y - chic[p][1])
            if temp > chic_distance:
                temp = chic_distance
        chic_sum += temp
    chicken_min.append(chic_sum)

print(min(chicken_min))