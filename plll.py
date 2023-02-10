def ispln(s1):
    if list(s1) == list(reversed(s1)):
        return 1
    return 0



# def garo(BRD):
#     for M in range(100, 1,-1):
#         for row in range(100):
#             for i in range(100 - M + 1):
#                 # temp = BRD[row][i:M + i]
#                 temp = ''
#                 cnt = 0
#                 for j in range(i, M + i):
#                     temp += BRD[row][j]
#                     cnt += 1
#                 if ispln(temp) == 1:
#                     cnt_lst.append(cnt)
#                     cnt_lst = set(cnt_lst)
#
#
# def sero(BRD):
#     for col in range(100):
#         for j in range(100 - M + 1):
#             temp = ''
#             cnt = 0
#             for k in range(M):
#                 temp += BRD[j + k][col]
#                 cnt += 1
#             if ispln(temp) == 1:
#                 cnt_lst.append(cnt)
#                 cnt_lst = set(cnt_lst)







# T = 10
for tc in range(1, 2):
    cnt_lst1 = []
    cnt_lst2 = []
    BRD = []
    # 2. 보드 만들기
    for brd in range(100):
        BRD.append(input())
    # print(BRD)
    # 3. 가로

    for M in range(100, 1,-1):
        for row in range(100):
            for i in range(100 - M + 1):
                # temp = BRD[row][i:M + i]
                temp = ''
                cnt = 0
                for j in range(i, M + i):
                    temp += BRD[row][j]
                    cnt += 1
                if ispln(temp) == 1:
                    cnt_lst1.append(cnt)
    # 4. 세로
        for col in range(100):
            for j in range(100 - M + 1):
                temp = ''
                cnt = 0
                for k in range(M):
                    temp += BRD[j + k][col]
                    cnt += 1
                if ispln(temp) == 1:
                    cnt_lst1.append(cnt)
                    cnt_lst2 = set(cnt_lst1)
    mmax = max(cnt_lst2)
    print(f'#{tc} {mmax}')




---------------------------------------------------

for test_case in range(1, 11):
    t = int(input())
    n = 100
    lst = [list(map(str, input())) for _ in range(n)]
    s = ''
    for m in range(1, 101):
        for i in range(n):
            for j in range(n - m + 1):
                ss = []
                count_row = 0
                count_col = 0
                for k in range(m // 2):
                    if lst[i][j + k] == lst[i][j + m - k - 1]:
                        count_row += 1
                    if lst[j + k][i] == lst[j + m - k - 1][i]:
                        count_col += 1
                 if count_row == m // 2:
                    s = "".join(lst[i][j:j + m])
                    break
                if count_col == m // 2:
                    for l in range(m):
                        ss.append(lst[j + l][i])
                    s = "".join(ss)
                    break

        print(f'#{test_case}', len(s))