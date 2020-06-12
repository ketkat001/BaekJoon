# 삼성 A형 코딩테스트 기출  시험 감독

N = int(input())
n_list = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0

for i in range(N):
    if B > C:
        if n_list[i] - B > 0:
            cnt += 1
            if (n_list[i] - B) % C > 0:
                cnt += ((n_list[i] - B) // C + 1)
            else:
                cnt += (n_list[i] - B) // C
        else:
            cnt += 1
    else:
        cnt += 1
        if (n_list[i] - B) % C > 0:
            cnt += (n_list[i] - B) // C + 1
        else:
            cnt += (n_list[i] - B) // C
print(cnt)