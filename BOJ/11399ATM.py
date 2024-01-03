n = int(input())
lst = list(map(int, input().split()))
lst.sort()

waitTime = 0
totalWaitTime =0
for i in lst:
    waitTime += i
    totalWaitTime += waitTime

print(totalWaitTime)
