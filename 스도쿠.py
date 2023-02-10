    # for row in range(10):
    #     for col in range(10):
    #         lst.remove(arr[row][col])
    # if lst == [] :
    #     ans1 = 1
    # else :
    #     ans1 = 0


T = int(input())
for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(10)]
    #가로탐색   

    #세로탐색




    #네모탐색








def garo(arr):
    lst = [1,2,3,4,5,6,7,8,9,10]
    for row in range(10):
        for col in range(10):
            lst.remove(arr[row][col])
    if lst == [] :
        ans1 = 1
        return ans1
    else :
        ans1 = 0
        return ans1
    
def sero(arr):
    lst = [1,2,3,4,5,6,7,8,9,10]
    for col in range(10):
        for row in range(10):
            lst.remove(arr[row][col])
    if lst == [] :
        ans = 1
        return ans
    else :
        ans = 0
        return ans
    
def nemo(arr):




칼럼
012  345 678
012  345 678
012  345 678

012
345
678

----------------
# list를 set으로 만들고
# 길이가 9가 아니면 ?
# len(set(lst)) != 9 스도쿠가 아니다
# for i in [0,3,6]:
#     for j in [0,3,6]: #가능한 모든시작
#         lst = arr[i][j:j+3] + [i+1]+....
#         lst(set(lst)) != 9: X


def solve(arr):
    for lst in arr:             # 행을 체크
        if len(set(lst))!=9:    # 스도쿠 실패
            return 0
 
    arr_t = list(zip(*arr))
    for lst in arr_t:           # 열을 체크
        if len(set(lst))!=9:    # 스도쿠 실패
            return 0

    for i in (0,3,6):
        for j in (0,3,6):       # 3*3 격자
            lst = arr[i][j:j+3]+arr[i+1][j:j+3]+arr[i+2][j:j+3]
            if len(set(lst))!=9:
                return 0
    return 1

T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = solve(arr)
    print(f'#{test_case} {ans}')