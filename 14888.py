# 삼성 A형 코딩테스트 연산자 끼워넣기
from itertools import permutations


def calculator(n1, n2, c):
    global save_num
    if c == 0:
        save_num = n1 + n2
    elif c == 1:
        save_num = n1 - n2
    elif c == 2:
        save_num = n1 * n2
    elif c == 3:
        upper = 1 if n1 < 0 and n1 % n2 else 0
        save_num = n1 // n2
        save_num += upper


N = int(input())
num_list = list(map(int, input().split()))
cal_list = list(map(int, input().split()))
cal = []
max_value = -1000000001
min_value = 1000000001
for i in range(4):
    for _ in range(cal_list[i]):
        cal.append(i)

cal_stack = list(permutations(cal, N-1))
for j in range(len(cal_stack)):
    num = num_list[:]
    save_num = num.pop(0)
    cal_l = list(cal_stack[j])
    while num:
        num_1 = save_num
        num_2 = num.pop(0)
        p = cal_l.pop()
        calculator(num_1, num_2, p)
    if save_num > max_value:
        max_value = save_num
    if save_num < min_value:
        min_value = save_num

print(max_value)
print(min_value)