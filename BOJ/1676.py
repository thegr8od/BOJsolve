#팩토리얼 0의 개수
import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))

sum = 1

for i in range(N):
    sum *= N
    N -= 1

sum = list(str(sum))
print(sum)
cnt = 0
while True:
    if(sum.pop() != '0'):
      break  
    cnt += 1


print(cnt)
