lst = [1,2,3,4,5,6,7,8,9]

def check(lst):
    if len(set(lst)) != 9:
        return  0
    return 1

def check(lst):
    confirms = [False] * 10
    for n in lst:
        if confirms[n]:
            return 0
        confirms[n] += 1
    return 1

for r in [0,3,6]:
    for j in [0,3,6]:
        lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
        if len(set(lst)) != 9:
            return 0

for i in [0,3,6]:
    for j in [0,3,6]:
        lst = []
        for r in range(i,i+3):
            for c in range(j,j+3):
                lst.append(arr[r][c])
        if
