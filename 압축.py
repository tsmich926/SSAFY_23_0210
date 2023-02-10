
# T = int(input())
# for test_case in range(1, T + 1):
#     arr = [0 for _ in range(10)]
#     print(arr)
#     len = 0
#     n = int(input())
#     for i in range(n):
#         lst1 = list(input().split())
#     print(lst1)
        # if M == 10:
        #     s1 = alpa * int(M)
        # else:
        #     while M > 0:
        #         s = alpa * int(M)
        #         M -= 1

T = int(input())
for test_case in range(1,1+T):
    result = ''
    total = 0
    for _ in range(int(input())):
        char,num = input().split()
        result += char*int(num)
        total += int(num)
    print(result)
    print(total)
    # print(f"#{test_case}")
    for i in range(total//10+1):
        print(i)
        print(result[10*i:10*(i+1)])