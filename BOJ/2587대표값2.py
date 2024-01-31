lst = []
for i in range(5):
    lst.append(int(input()))

sum = 0
lst.sort()
for i in lst:
    sum += i

print(int(sum/len(lst)))
print(lst[2])