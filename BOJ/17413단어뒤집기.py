import sys
input = sys.stdin.readline

word = input().rstrip()
word_stack = []
tag = False
res = ''

for s in word:
    if s == " ":
        while word_stack:
            res += word_stack.pop()
        res += s
    elif s == "<":
        while word_stack:
            res += word_stack.pop()
        tag = True
        res += s
    elif s == ">":
        tag = False
        res += s
    elif tag:
        res += s
    else:
        word_stack.append(s)
        
print(res)
