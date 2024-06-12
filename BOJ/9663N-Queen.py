n = int(input())
cnt = 0
row = [0] * n

def promising(r):
    for i in range(r):
        #세로 체크
        if row[i] == row[r]:
            return False
        #대각선 체크
        if abs(r - i) == abs(row[r] - row[i]):
            return False
    return True

def n_queen(r):
    global cnt
    
    if r == n:
        cnt += 1
        return
    
    for i in range(n):
        row[r] = i
        if promising(r):
            n_queen(r + 1)
    
n_queen(0)
print(cnt)