t = int(input())
ans = 1
for i in range(t):
    a, b = map(int, input().split())
    if a == ans :
        ans = b
    elif b == ans :
        ans = a
        
print(ans)
        