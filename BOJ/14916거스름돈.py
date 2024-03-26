n = int(input())

ans = 0

if n % 5 == 0:
    ans = n // 5
elif n % 2 == 0:
    ans += n // 5
    n = n % 5
    ans += n // 2
else:
    while n % 2 != 0:
        ans +=1
        n -= 5
        if n < 0:
            ans = -1
            break
    ans += n //2
    
print(ans)