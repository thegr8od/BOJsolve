n,m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
ans = []


def binary_search(start,end,cnt):
    while start <= end:
        cnt = 0
        mid = (start+end) // 2
        for i in data:
            if i >= mid:
                cnt += i - mid
                
        if cnt >= m:
            ans.append(mid)
            start = mid + 1
        else:
            end = mid - 1
        
            
binary_search(0,data[-1],0)
print(max(ans))        
            