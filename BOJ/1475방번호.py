n = input()
lst = [int(digit) for digit in str(n)]

cnt = 0
sixNine = 0
for i in lst:
    if i == 6 or i == 9:
        sixNine += 0.5
    else:
        cnt += 1

print(round(sixNine) + cnt)