import sys
input = sys.stdin.readline

n,k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

sum = 0
for i in coin[::-1]:
    sum += (int(k / i))
    k = (k % i)

print(sum)



