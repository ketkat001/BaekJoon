# 삼성 A형 코딩테스트  퇴사
def solve(a, v, idx, t):
    global max_value
    if max_value < v:
        max_value = v
    if a < 0 or idx == N:
        return
    else:
        if t > 0:
            solve(a, v, idx+1, t-1)
        else:
            if a - time_list[idx] >= 0 and t == 0:
                solve(a - time_list[idx], v + pay_list[idx], idx + 1, t + time_list[idx] - 1)
            solve(a-1, v, idx+1, t)


N = int(input())
time_list = []
pay_list = []
max_value = 0
for _ in range(N):
    T, P = map(int, input().split())
    time_list.append(T)
    pay_list.append(P)
solve(N, 0, 0, 0)
print(max_value)