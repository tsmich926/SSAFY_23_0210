#원래 배열을 90도로 회전하는 함수
def nine(arr):




T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr= [list(map(int,input().split())) for _ in range(n)]

--------------
#90도 회전
arr1[i][j] = arr[N-1-j][i]

#180도 회전
arr2[i][j] = arr[N-1-i][N-1-j]

#270회전
arr3[i][j] = arr[j][N-1-i]

#출력?
for a,b,c in zip(a1,a2,a3)
{"".join(a)} _{"".join(b)}


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr= [input().split() for _ in range(N)]
    a1 = [[0]*N for _ in range(N)]
    a2 = [[0]*N for _ in range(N)]
    a3 = [[0]*N for _ in range(N)]

    #회전각도에 따른 위치값을 저장
    for i in range(N):
        for j in range(N):
            a1[N][j] = arr[N-1-j][i]
            a2[i][j] = arr[N-1-i][N-1-j]
            a3[i][j] = arr[j][N-1-i]
    print(f'{tc}')
    for a,b,c in zip(a1,a2,a3):
        print(f'{"".join(a)}')





#정답코드
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    a1 = [[0]*N for _ in range(N)]  # 90도
    a2 = [[0]*N for _ in range(N)]
    a3 = [[0]*N for _ in range(N)]
 
    # 회전각도에 따른 위치값을 저장
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]
            a2[i][j] = arr[N-1-i][N-1-j]
            a3[i][j] = arr[j][N-1-i]
    print(f'#{test_case}')
    for a,b,c in zip(a1,a2,a3):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')

