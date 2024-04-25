
def power(n,m):
    if m == 1:
        return n
    else:
        return power(n,m-1) * n
    
print(power(2,4))