import sys
input = sys.stdin.readline

m = int(input())
s= set()

for i in range(m):
    lst = list(input().split())
    cmd = lst[0]
    if cmd == 'add':
        s.add(int(lst[1]))
    elif cmd =='remove':
        try:
            s.remove(int(lst[1]))
        except:
            pass
    elif cmd == 'check':
        if int(lst[1]) in s:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if int(lst[1]) in s:
            s.remove(int(lst[1]))
        else:
            s.add(int(lst[1]))
    elif cmd == 'all':
        s = set([i for i in range(1,21)])
    else:
        s = set()

