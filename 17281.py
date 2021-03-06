from itertools import permutations


N = int(input())
score_idx = [list(map(int, input().split())) for _ in range(N)]
max_score = 0
for m_l in permutations([1, 2, 3, 4, 5, 6, 7, 8]):
    m_l = list(m_l)
    m_l.insert(3, 0)
    num = 0
    i = 0
    for inning in score_idx:
        base1, base2, base3 = 0, 0, 0
        out_cnt = 0
        while out_cnt < 3:
            if inning[m_l[i]] == 0:
                out_cnt += 1
            elif inning[m_l[i]] == 1:
                num += base3
                base1, base2, base3 = 1, base1, base2
            elif inning[m_l[i]] == 2:
                num += base2 + base3
                base1, base2, base3 = 0, 1, base1
            elif inning[m_l[i]] == 3:
                num += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            elif inning[m_l[i]] == 4:
                num += base1 + base2 + base3 + 1
                base1, base2, base3 = 0, 0, 0
            i = (i + 1) % 9
    max_score = max(max_score, num)
print(max_score)