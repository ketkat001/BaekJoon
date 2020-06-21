# 삼성 A형 기출 문제 17140번 이차원 배열과 연산
def solve(cnt, arr):
    global result
    if cnt > 100:
        return
    if r-1 < len(arr) and c-1 < len(arr[0]):
        if arr[r-1][c-1] == k:
            result = cnt
            return
    if len(arr) >= len(arr[0]):
        arr = solve2(arr)
        solve(cnt+1, arr)
    else:
        arr = list(zip(*arr))
        arr = solve2(arr)
        arr = list(zip(*arr))
        solve(cnt+1, arr)


def solve2(arr):
    arr_temp = []
    max_length = 3
    for i in range(len(arr)):
        temp_list = [0]*101
        temp = []
        for num in arr[i]:
            if num != 0:
                temp_list[num] += 1
        temp_list = list(enumerate(temp_list))
        temp_list.sort(key=lambda x: x[1])

        for j in range(len(temp_list)):
            if temp_list[j][1] != 0:
                temp.append(temp_list[j][0])
                temp.append(temp_list[j][1])
        max_length = max(max_length, len(temp))
        arr_temp.append(temp)
    if max_length < 3:
        max_length = 3
    elif max_length > 100:
        max_length = 100

    n_arr = [[0]*max_length for _ in range(len(arr))]
    for p in range(len(arr_temp)):
        for q in range(len(arr_temp[p])):
            n_arr[p][q] = arr_temp[p][q]
    return n_arr


r, c, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(3)]
result = -1
solve(0, array)
print(result)
