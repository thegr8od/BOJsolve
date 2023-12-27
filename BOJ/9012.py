import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    lst = input().rstrip('\n')
    cnt = 0
    for i in lst:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1  
            if cnt < 0:
                print("NO")
                break
   

    if cnt == 0:
        print("YES")
    elif cnt > 0:
        print("NO")
