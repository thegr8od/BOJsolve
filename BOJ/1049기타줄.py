n,m = map(int,(input().split()))
lst = []
for i in range(m):
    lst.append(list(map(int, input().split())))


min6 = 2000
min1 = 2000

for i in lst:
    if i[0] <= min6:
        min6 = i[0]
    if i[1] <= min1:
        min1 = i[1]

sum = 0
if min6 < min1 * 6:
    sum += min6 * (n / 6)
    sum += min1 * (n % 6)
else:
    sum += min1 * n

print(sum)