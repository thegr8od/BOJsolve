#1359 복권 (구글 참고했습니다 ㅠㅠ)
from itertools import combinations

n,m,k = map(int, input().split())

data = [*combinations([i for i in range(1,n+1)],m)]

ans = 0
for i in data:
    cnt = 0
    for j in range(m):
        if i[j] < m+1:
            cnt += 1
    if cnt >= k:
        ans += 1

print(ans/len(data))  