# def ispellin(s):
#     if list(s) == list(s.reversed(s)):
#         return 1
#     return 0
#
# for tc in range(1,2):
#     N = int(input())
#     BRD = []
#     # 2. 보드 만들기
#     for brd in range(11):
#         BRD.append(input())
#     #가로 탐색
#     lst= []
#     for m in range(1, 101):
#         for row in range(101):
#             for j in range(101-m+1):
#                 temp = " "
#                 for k in range(j,m+j):
#                     temp += BRD[row][k]
#             if ispellin(temp) == 1:
#                 lst.append(temp)
#     print(lst)



def ispln(s1):
    if list(s1) == list(reversed(s1)):
        return 1
    return 0


# T = 10
for tc in range(1,2):
    cnt_lst= []
    BRD = []
    # 2. 보드 만들기
    for brd in range(100):
        BRD.append(input())
    # print(BRD)
    # 3. 가로

    for M in range(1,100):
        for row in range(100):
            for i in range(100 - M + 1):
                # temp = BRD[row][i:M + i]
                temp = ''
                cnt = 0
                for j in range(i, M + i):
                    temp += BRD[row][j]
                    cnt += 1
                if ispln(temp) == 1:
                    cnt_lst.append(cnt)
                    cnt_lst1 = set(cnt_lst)

    # print(cnt_lst1)

    # # 4. 세로
    # for M in range(1,100):
    #     for col in range(100):
    #         for j in range(100 - M + 1):
    #             temp = ''
    #             cnt = 0
    #             for k in range(M):
    #                 temp += BRD[j + k][col]
    #                 cnt += 1
    #             if ispln(temp) == 1:
    #                 cnt_lst.append(cnt)
    #
    # mmax = max(cnt_lst)
    # print(f'#{tc} {mmax}')