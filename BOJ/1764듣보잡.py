import sys

input = sys.stdin.readline

n,m = map(int, input().split())

lst = []
lst2 = []


for i in range(n):
    lst.append(input().rstrip())

for j in range(m):
    lst2.append(input().rstrip())

answer = list(set(lst) & set(lst2))
answer.sort()

print(len(answer))
print(*answer, sep='\n')