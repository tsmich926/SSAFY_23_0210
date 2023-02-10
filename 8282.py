import sys
sys.stdin = open("gago.txt", "r")

# 3x3일때는 적용안됨
#####고치자
T = int(input())
lst = []
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #우,하,좌,상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

