#체스판 다시 칠하기
import sys
input = sys.stdin.readline

N,M = map(int, input().split())

lst = []
result = []

for i in range(N):
    lst.append(input().rstrip())

for i in range(N-7):
    for j in range(M-7):
        black_idx = 0
        white_idx = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 ==0:
                    if lst[a][b] != 'B':
                        black_idx += 1
                    if lst[a][b] != 'W':
                        white_idx +=1
                else:
                    if lst[a][b] != 'W':
                        black_idx +=1
                    if lst[a][b] != 'B':
                        white_idx +=1
        result.append(black_idx)
        result.append(white_idx)

print(min(result))