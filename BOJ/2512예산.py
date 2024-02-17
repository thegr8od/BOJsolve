def binary_search(array, target, start, end):
    result = 0
    while start<=end:
        total = 0
        mid = (start + end) // 2
        for x in array:
            if x <= mid:
                total += x
            else:
                total += mid
        
        if total > target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

n = int(input())
data = list(map(int, input().split()))
total = int(input())
data.sort()
print(binary_search(data, total, 1, data[-1]))

