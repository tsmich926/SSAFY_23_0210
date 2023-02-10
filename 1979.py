#어디에 단어가 들어갈 수 있을까
#cnt가 끝나면 길이 비교 :0인경우 or 끝 경계idx인 경우
#arr[]==1 cnt+=1,arr[]==0  cnt==k cnt==0
arr= [list(map(int,input().split()))]

#arr에서 한행을 꺼낸다
# ans = 0
# for lst in arr:
#     cnt = 0
#     for n in lst:
#         if n != 0:
#             cnt += 1
#         else:
#             if cnt == k :
#                 ans += 1
#                 cnt = 0

def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
            else : #칸 없음!
                if cnt == k:
                    ans += 1
                cnt = 0
    return ans
                


T = int(input())
for tc in range(1,1+T):
    N,K = map(int,input().split())
    arr =[list(map(int,input().split()))] + [0]

    #arr과 arr_t로 각각 개수를 계산
    arr_t = list(map (list,zip(*arr )))
    # ans count(arr) + count(arr_t)
    print(f'#{tc} {ans}')

---------------------------------------------
def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:      # 단어를 넣을 수 있는 공백
                cnt += 1
            else:           # 칸 없음!
                if cnt==K:
                    ans += 1
                cnt=0
    return ans

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]

    # arr와 arr_t 로 각각 개수를 계산
    arr_t = list(map(list,zip(*arr)))
    ans = count(arr) + count(arr_t)
    print(f'#{test_case} {ans}')