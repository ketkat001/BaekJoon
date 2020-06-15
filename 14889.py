# 삼성 A형 코딩 테스트 기출 : 스타트와 링크
from itertools import combinations


def solve(m1):
    global min_value
    m1 = list(m1)
    m2 = []
    m1_value, m2_value = 0, 0
    for mem in n_list:
        if mem not in m1:
            m2.append(mem)
    for p in range(N//2-1):
        for q in range(p, N//2):
            m1_value += status[m1[p]][m1[q]] + status[m1[q]][m1[p]]
            m2_value += status[m2[p]][m2[q]] + status[m2[q]][m2[p]]
    if min_value > abs(m1_value - m2_value):
        min_value = abs(m1_value - m2_value)


N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]
n_list = [i for i in range(N)]
member_list = list(combinations(n_list, N//2))
min_value = 100000
for m in member_list:
    solve(m)
print(min_value)