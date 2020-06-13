# 삼성 A형 코딩 테스트 : 주사위 굴리기
def is_wall(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False


def solve(d_top, d_east, d_north, d_west, d_south, d_bottom, d_x, d_y):
    for di in direction_list:
        next_d_x = d_x + dx[di]
        next_d_y = d_y + dy[di]
        if di == 1:  # 오른쪽으로 굴릴경우
            if is_wall(next_d_x, next_d_y):
                d_top, d_east, d_north, d_west, d_south, d_bottom = d_west, d_top, d_north, d_bottom, d_south, d_east
                if map_list[next_d_x][next_d_y] == 0:
                    map_list[next_d_x][next_d_y] = d_bottom
                else:
                    d_bottom = map_list[next_d_x][next_d_y]
                    map_list[next_d_x][next_d_y] = 0
                print(d_top)
            else:
                continue
        if di == 2:  # 왼쪽으로 굴릴경우
            if is_wall(next_d_x, next_d_y):
                d_top, d_east, d_north, d_west, d_south, d_bottom = d_east, d_bottom, d_north, d_top, d_south, d_west
                if map_list[next_d_x][next_d_y] == 0:
                    map_list[next_d_x][next_d_y] = d_bottom
                else:
                    d_bottom = map_list[next_d_x][next_d_y]
                    map_list[next_d_x][next_d_y] = 0
                print(d_top)
            else:
                continue
        if di == 3:  # 위로 굴릴경우
            if is_wall(next_d_x, next_d_y):
                d_top, d_east, d_north, d_west, d_south, d_bottom = d_north, d_east, d_bottom, d_west, d_top, d_south
                if map_list[next_d_x][next_d_y] == 0:
                    map_list[next_d_x][next_d_y] = d_bottom
                else:
                    d_bottom = map_list[next_d_x][next_d_y]
                    map_list[next_d_x][next_d_y] = 0
                print(d_top)
            else:
                continue
        if di == 4:  # 아래로 굴릴경우
            if is_wall(next_d_x, next_d_y):
                d_top, d_east, d_north, d_west, d_south, d_bottom = d_south, d_east, d_top, d_west, d_bottom, d_north
                if map_list[next_d_x][next_d_y] == 0:
                    map_list[next_d_x][next_d_y] = d_bottom
                else:
                    d_bottom = map_list[next_d_x][next_d_y]
                    map_list[next_d_x][next_d_y] = 0
                print(d_top)
            else:
                continue
        d_x, d_y = next_d_x, next_d_y


dice_top, dice_east, dice_north, dice_west, dice_south, dice_bottom = 0, 0, 0, 0, 0, 0   # 초기 주사위 상태
dx = [0, 0, 0, -1, 1]   # 방향 빈값, 동, 서, 북, 남
dy = [0, 1, -1, 0, 0]
N, M, dice_x, dice_y, K = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
direction_list = list(map(int, input().split()))
solve(dice_top, dice_east, dice_north, dice_west, dice_south, dice_bottom, dice_x, dice_y)


