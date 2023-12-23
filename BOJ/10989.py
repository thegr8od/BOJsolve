import sys
input = sys.stdin.readline
N = int(input())

lst = []

for i in range(N):
    n = int(input())
    lst.append(n)


lst = list(set(lst))
lst.sort()
print(*lst, sep='\n')





