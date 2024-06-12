from itertools import permutations

n = int(input())

for row in permutations([i for i in range(1,n+1)],n):
    print(*row)