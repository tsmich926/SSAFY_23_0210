import sys
sys.stdin = open("jip.txt", "r")
T = int(input())
lst = []
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for row in range(N):
        #현재 좌표: row, col
        for col in range(M):
            sum = 0
            sum += arr[row][col]
            for d in range(4):
                newR = row + dr[d]
                newC = col + dc[d]
                if 0 <= newR < N and 0 <= newC < M:
                    sum += arr[newR][newC]
            lst.append(sum)
    mmax = 0
    for k in range(len(lst)):
        if mmax < lst[k]:
            mmax = lst[k]
    print(f'#{test_case} {mmax}')