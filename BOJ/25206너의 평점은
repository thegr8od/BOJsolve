lst = []
for i in range(20):
    lst.append(input().split())


num = 0
grade = 0
for i in lst:
    num += float(i[1])
    if i[2] == "A+":
        grade += float(i[1]) * 4.5
    elif i[2] == "A0":
        grade += float(i[1]) * 4.0
    elif i[2] == "B+":
        grade += float(i[1]) * 3.5
    elif i[2] == "B0":
        grade += float(i[1]) * 3.0
    elif i[2] == "C+":
        grade += float(i[1]) * 2.5
    elif i[2] == "C0":
        grade += float(i[1]) * 2.0
    elif i[2] == "D+":
        grade += float(i[1]) * 1.5
    elif i[2] == "D0":
        grade += float(i[1]) * 1.0
    elif i[2] == "F":
        grade += float(i[1]) * 0.0
    else:
        num -= float(i[1]) 
                            
print(grade/num)