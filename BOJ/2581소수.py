#소수 구하기
import math

m = int(input())
n = int(input())
data = []

for i in range(m, n+1):
    if i == 1: #1일 경우 진행
        continue
    for j in range(2, int(math.sqrt(i))+1): #n의 루트까지만 확인하면 됨
        if i % j == 0:
            break

    else:
        data.append(i)

if len(data) == 0:
    print(-1)
else:
    print(sum(data))
    print(min(data))