def ispellin(s):
    if list(s) == list(s.reversed(s)):
        return 1
    return 0

for tc in range(1,11):
    N = int(input())
    arr= [input() for _ in range(101)]
    #가로 탐색
    lst= []
    for m in range(1, 101)
        for row in range(101):
            for j in range(101-m+1):
                temp = " "
                for k in range(j,m+j)
                    temp += arr[row][k]
            if ispellin(temp) == 1:
                lst.append(temp)



    T = 10
    for tc in range(1, T + 1):
        M = int(input())
        BRD = []
        cnt = 0
        # 2. 보드 만들기
        for brd in range(8):
            BRD.append(input())
        # 3. 가로
        for row in range(8):
            for i in range(8 - M + 1):
                # temp = BRD[row][i:M + i]
                temp = ''
                for j in range(i, M + i):
                    temp += BRD[row][j]
                if ispln(temp) == 1:
                    cnt += 1
        # 4. 세로
        for col in range(8):
            for j in range(8 - M + 1):
                temp = ''
                for k in range(M):
                    temp += BRD[j + k][col]
                if ispln(temp) == 1:
                    cnt += 1
        print(f'#{tc} {cnt}')
