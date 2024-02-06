n = input()
lst = [int(i) for i in n]
lst.sort(reverse=True)
print(*lst, sep='')