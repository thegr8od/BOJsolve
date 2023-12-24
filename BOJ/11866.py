N, K = map(int, input().split())
lst = list(range(1, N+1))
result = []
idx = 0

while len(lst) != 0:
    idx += (K-1)
    idx = idx % len(lst)
    result.append(lst.pop(idx))

print("<", end="")
for i in range(0, N-1):
    print(result[i], end = ", ")
print(result[N-1], end=''+">")