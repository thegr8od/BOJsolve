n = int(input())

data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

data1.sort()
data2.sort(reverse=True)

sum = 0 
for i in range(n):
    sum += data1[i] * data2[i]

print(sum)
