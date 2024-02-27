n, r, c = map(int, input().split())
cnt = 0


def recursion(start_r,start_c,start_n):
    global cnt
    if start_n == 2:
        if start_r == r and start_c == c:
            print(cnt)
            return
        cnt += 1
        if start_r == r and start_c + 1 == c:
            print(cnt)
            return
        cnt += 1
        if start_r + 1 == r and start_c == c:
            print(cnt)
            return
        cnt += 1
        if start_r + 1 == r and start_c + 1 == c:
            print(cnt)
            return
        cnt += 1
    else:
        start_n //= 2
        recursion(start_r, start_c, start_n)
        recursion(start_r, start_c + start_n, start_n)
        recursion(start_r + start_n, start_c, start_n)
        recursion(start_r + start_n, start_c + start_n, start_n)

recursion(0,0, 2 ** n)