n = int(input())
m = int(input())
data = input()

i, cnt, ans = 0,0,0

while i < m-1:
    if data[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
        
print(ans)