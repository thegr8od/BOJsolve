T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    
    candy_count = 0 

    if arr[1] < 2 or arr[2] < 3: 
        print(f"#{test_case} -1")
        continue

    if arr[2] - arr[1] <= 0:  
        candy_count += arr[1] - arr[2] + 1
        arr[1] = arr[2] - 1  

    if arr[1] - arr[0] <= 0: 
        candy_count += arr[0] - arr[1] + 1
        arr[0] = arr[1] - 1 

    print(f"#{test_case} {candy_count}")