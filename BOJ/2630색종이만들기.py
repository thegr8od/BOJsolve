import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

result = []

def recursion(x,y,n):
    color = data[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != data[i][j]:
                recursion(x, y, n//2)
                recursion(x, y+n//2, n//2)
                recursion(x+n//2, y, n//2)
                recursion(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        result.append(0)
    else :
        result.append(1)

recursion(0,0,n)
print(result.count(0))
print(result.count(1))