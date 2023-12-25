import sys
input = sys.stdin.readline

N, K = map(int, input().split())

result = 1

for i in range(K):
    result *= (N-i)

divide = 1

for i in range(1,K+1):
    divide *= i

print(int(result / divide))


