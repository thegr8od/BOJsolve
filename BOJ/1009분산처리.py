n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    num = 1
    for j in range(b):
        num *= a
        if num >= 10:
            num = num % 10
            if num % 10 == 0:
                num = 10        
    print(num)