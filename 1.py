score_idx = [list(map(int, input().split())) for _ in range(2)]
num = 0
ln = [1, 2, 3, 4, 5, 6, 7, 8]
ln.insert(3, 0)
s_l = score_idx[:]
i = 0
while s_l:
    base = [0, 0, 0]
    out_cnt = 0
    while out_cnt < 3:
        if i >= 9:
            i = 0
        if s_l[0][ln[i]] == 0:
            out_cnt += 1
            if out_cnt >= 3:
                break
        elif s_l[0][ln[i]] == 1:
            if base[0] == 0:
                base[0] += 1
            if base[0] == 1:
                base[0] -= 1
                base[1] += 1
            if base[1] == 1:
                base[1] -= 1
                base[2] += 1
            if base[2] == 1:
                base[2] -= 1
                num += 1
        elif s_l[0][ln[i]] == 2:
            if base[1] == 0:
                base[1] += 1
            if base[0] == 1:
                base[2] += 1
            if base[1] == 1:
                base[1] -= 1
                num += 1
            if base[2] == 1:
                base[2] -= 1
                num += 1
        elif s_l[0][ln[i]] == 3:
            if base[0] == 1:
                base[0] -= 1
                num += 1
            if base[1] == 1:
                base[1] -= 1
                num += 1
            if base[2] == 1:
                base[2] -= 1
                num += 1
            if base[2] == 0:
                base[2] += 1
        elif s_l[0][ln[i]] == 4:
            if base[0] == 1:
                base[0] -= 1
                num += 1
            if base[1] == 1:
                base[1] -= 1
                num += 1
            if base[2] == 1:
                base[2] -= 1
                num += 1
            num += 1
        i += 1
    s_l.pop(0)
print(num)